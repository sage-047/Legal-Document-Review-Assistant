import fitz  # PyMuPDF
import docx

def extract_text_from_pdf(file_path: str) -> str:
    """Read text from a PDF file."""
    text = ""
    try:
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
    except Exception as e:
        return f"Error reading PDF: {e}"
    return text

def extract_text_from_docx(file_path: str) -> str:
    """Read text from a DOCX file."""
    text = ""
    try:
        doc = docx.Document(file_path)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except Exception as e:
        return f"Error reading DOCX: {e}"
    return text
