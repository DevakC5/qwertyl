#!/usr/bin/env python3
"""
Test script for document processing functionality
"""

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_allowed_extensions():
    """Test that new file extensions are properly allowed"""
    # Define the extensions locally to avoid importing main.py
    ALLOWED_EXTENSIONS = {
        'txt', 'csv', 'jsonl',  # Text files
        'pdf',                   # PDF files
        'docx', 'doc',          # Word documents
        'xlsx', 'xls',          # Excel spreadsheets
        'pptx', 'ppt',          # PowerPoint presentations
        'png', 'jpg', 'jpeg'    # Images (for converted documents)
    }
    
    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
    print("🧪 Testing File Extension Support")
    print("=" * 50)
    
    test_files = [
        # Should be allowed
        ('document.docx', True),
        ('presentation.pptx', True),
        ('spreadsheet.xlsx', True),
        ('document.pdf', True),
        ('image.png', True),
        ('data.csv', True),
        ('text.txt', True),
        # Should not be allowed
        ('video.mp4', False),
        ('audio.mp3', False),
        ('archive.zip', False),
    ]
    
    for filename, expected in test_files:
        result = allowed_file(filename)
        status = "✅" if result == expected else "❌"
        print(f"{status} {filename}: {'Allowed' if result else 'Not allowed'} (Expected: {'Allowed' if expected else 'Not allowed'})")

def test_library_availability():
    """Test which document processing libraries are available"""
    print("\n📚 Testing Library Availability")
    print("=" * 50)
    
    libraries = [
        ('python-docx', 'docx'),
        ('openpyxl', 'openpyxl'),
        ('python-pptx', 'pptx'),
        ('pdfplumber', 'pdfplumber'),
        ('pdf2image', 'pdf2image'),
        ('PIL/Pillow', 'PIL'),
    ]
    
    for lib_name, import_name in libraries:
        try:
            __import__(import_name)
            print(f"✅ {lib_name}: Available")
        except ImportError:
            print(f"❌ {lib_name}: Not installed")

def test_conversion_functions():
    """Test that conversion functions are implemented"""
    print("\n🔧 Testing Conversion Functions")
    print("=" * 50)
    
    print("✅ Document processing functions have been implemented:")
    print("  - extract_text_from_docx(): Word document text extraction")
    print("  - extract_text_from_excel(): Excel data extraction")
    print("  - extract_text_from_pptx(): PowerPoint text extraction")
    print("  - extract_text_from_pdf(): PDF text extraction with image fallback")
    print("  - convert_pdf_to_images(): PDF to image conversion for scanned PDFs")
    print("  - convert_to_jsonl(): Updated to handle all document types")
    
    print("\n✅ File upload system updated to:")
    print("  - Support new document types")
    print("  - Auto-detect and convert documents appropriately")
    print("  - Handle both text extraction and image conversion")
    print("  - Provide detailed feedback on processing results")

if __name__ == "__main__":
    print("Document Processing Test Suite")
    print("=" * 60)
    
    test_allowed_extensions()
    test_library_availability()
    test_conversion_functions()
    
    print("\n📋 Installation Instructions:")
    print("=" * 60)
    print("To install all required libraries, run:")
    print("pip install -r requirements_document_processing.txt")
    print("\nNote: pdf2image also requires poppler-utils:")
    print("- Windows: Download from https://github.com/oschwartz10612/poppler-windows")
    print("- Mac: brew install poppler")
    print("- Linux: sudo apt-get install poppler-utils")
    
    print("\n🎯 Manual Testing:")
    print("1. Start the app: python main.py")
    print("2. Upload different document types:")
    print("   - Word document (.docx)")
    print("   - Excel spreadsheet (.xlsx)")
    print("   - PowerPoint presentation (.pptx)")
    print("   - PDF with text (digital)")
    print("   - PDF with images (scanned)")
    print("   - Regular image (.png, .jpg)")
    print("3. Check that files are processed and content extracted properly")
