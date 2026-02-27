import streamlit as st
import tempfile

from extract_text import extract_text_from_pdf, extract_text_from_docx
from playbook import PLAYBOOK
from prompts import build_review_prompt
from review_engine import review_contract
from pdf_generator import generate_pdf_report


st.set_page_config(page_title="AI Legal Review Assistant", layout="wide", page_icon="⚖️")

# Header
st.title("⚖️ AI Legal Document Review Assistant")
st.markdown("Upload your legal contract and I'll provide a comprehensive analysis with risk assessment and recommendations.")

# Sidebar for upload
with st.sidebar:
    st.header("📂 Upload Document")
    uploaded = st.file_uploader("Choose a contract (PDF or DOCX)", type=["pdf", "docx"])
    
    if uploaded:
        st.success(f"✅ Loaded: {uploaded.name}")
        
        # Extract contract text
        with tempfile.NamedTemporaryFile(delete=False) as tmp:
            tmp.write(uploaded.read())
            file_path = tmp.name

        if uploaded.name.lower().endswith(".pdf"):
            contract_text = extract_text_from_pdf(file_path)
        else:
            contract_text = extract_text_from_docx(file_path)

        if not contract_text.strip():
            st.error("❌ No readable text found in the document.")
            st.stop()
        
        # Show text preview in sidebar
        with st.expander("📄 View Extracted Text Preview"):
            st.text_area("First 1500 characters:", contract_text[:1500], height=200)

# Main content area
if not uploaded:
    # Welcome screen
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### 🔍 Smart Analysis")
        st.write("AI-powered review of contract clauses, risks, and compliance issues")
    
    with col2:
        st.markdown("### 💬 Clear Insights")
        st.write("Conversational explanations that anyone can understand")
    
    with col3:
        st.markdown("### 📄 PDF Reports")
        st.write("Download professional reports for your records")
    
    st.markdown("---")
    st.info("👈 Upload a contract in the sidebar to get started!")

else:
    # Review button
    if st.button("🚀 Start AI Review", type="primary", use_container_width=True):
        with st.spinner("🤖 Analyzing your contract... This may take a minute..."):
            prompt = build_review_prompt(contract_text, PLAYBOOK)
            review_output = review_contract(prompt)

        # Store in session state
        st.session_state['review_output'] = review_output
        st.session_state['contract_name'] = uploaded.name

    # Display review if available
    if 'review_output' in st.session_state:
        st.markdown("---")
        
        # Chat-style display
        st.markdown("### 💬 Review Analysis")
        
        # Display as a chat message from assistant
        with st.chat_message("assistant", avatar="⚖️"):
            st.markdown(st.session_state['review_output'])
        
        st.markdown("---")
        
        # Download section
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### 📥 Download Report")
            st.write("Save this comprehensive analysis as a PDF for your records.")
        
        with col2:
            # Generate PDF
            try:
                pdf_bytes = generate_pdf_report(
                    st.session_state['review_output'],
                    st.session_state['contract_name']
                )
                
                st.download_button(
                    label="📄 Download PDF Report",
                    data=pdf_bytes,
                    file_name=f"legal_review_{st.session_state['contract_name']}.pdf",
                    mime="application/pdf",
                    type="primary",
                    use_container_width=True
                )
            except Exception as e:
                st.error(f"Error generating PDF: {str(e)}")
        
        # Option to review another document
        st.markdown("---")
        if st.button("📝 Review Another Document"):
            del st.session_state['review_output']
            del st.session_state['contract_name']
            st.rerun()

