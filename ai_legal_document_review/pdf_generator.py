from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from io import BytesIO
from datetime import datetime


def generate_pdf_report(review_text: str, contract_name: str) -> bytes:
    """
    Generate a PDF report from the review text.
    Returns PDF as bytes.
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter,
                           rightMargin=72, leftMargin=72,
                           topMargin=72, bottomMargin=18)
    
    # Container for the 'Flowable' objects
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom title style
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='#1a1a1a',
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # Custom heading style
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        textColor='#2c3e50',
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    # Body text style
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=11,
        textColor='#333333',
        spaceAfter=12,
        leading=16
    )
    
    # Add title
    title = Paragraph("AI Legal Document Review Report", title_style)
    elements.append(title)
    elements.append(Spacer(1, 12))
    
    # Add metadata
    meta_text = f"<b>Document:</b> {contract_name}<br/><b>Review Date:</b> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}"
    meta = Paragraph(meta_text, body_style)
    elements.append(meta)
    elements.append(Spacer(1, 20))
    
    # Process the review text
    # Convert markdown-style formatting to reportlab format
    lines = review_text.split('\n')
    
    for line in lines:
        line = line.strip()
        if not line:
            elements.append(Spacer(1, 6))
            continue
            
        # Handle headers (markdown ##)
        if line.startswith('## '):
            header_text = line[3:].strip()
            elements.append(Paragraph(header_text, heading_style))
        elif line.startswith('# '):
            header_text = line[2:].strip()
            elements.append(Paragraph(header_text, title_style))
        # Handle bold text and bullet points
        elif line.startswith('- **') or line.startswith('* **'):
            # Bullet point with bold
            clean_line = line[2:].strip()
            elements.append(Paragraph(f"• {clean_line}", body_style))
        elif line.startswith('- ') or line.startswith('* '):
            # Regular bullet point
            clean_line = line[2:].strip()
            elements.append(Paragraph(f"• {clean_line}", body_style))
        else:
            # Regular paragraph
            elements.append(Paragraph(line, body_style))
    
    # Build PDF
    doc.build(elements)
    
    # Get PDF bytes
    pdf_bytes = buffer.getvalue()
    buffer.close()
    
    return pdf_bytes
