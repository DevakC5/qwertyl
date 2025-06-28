#!/usr/bin/env python3
"""
Test script for ReportLab PDF generation functionality
"""

import sys
import os

def test_reportlab_availability():
    """Test if ReportLab is properly installed"""
    print("🧪 Testing ReportLab Availability")
    print("=" * 50)
    
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter, A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        print("✅ ReportLab core modules imported successfully")
        
        # Test basic functionality
        from reportlab.platypus import Table, TableStyle
        from reportlab.lib import colors
        from reportlab.lib.units import inch
        print("✅ ReportLab advanced modules imported successfully")
        
        return True
    except ImportError as e:
        print(f"❌ ReportLab import failed: {e}")
        return False

def test_basic_pdf_generation():
    """Test basic PDF generation with ReportLab"""
    print("\n📄 Testing Basic PDF Generation")
    print("=" * 50)
    
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.pagesizes import letter
        
        # Create a simple PDF
        test_file = "test_report.pdf"
        c = canvas.Canvas(test_file, pagesize=letter)
        c.drawString(100, 750, "Hello ReportLab!")
        c.drawString(100, 730, "This is a test PDF generated with ReportLab")
        c.save()
        
        if os.path.exists(test_file):
            print("✅ Basic PDF generation successful")
            os.remove(test_file)  # Clean up
            return True
        else:
            print("❌ PDF file not created")
            return False
            
    except Exception as e:
        print(f"❌ Basic PDF generation failed: {e}")
        return False

def create_sample_reportlab_code():
    """Create sample ReportLab code examples"""
    print("\n📝 Sample ReportLab Code Examples")
    print("=" * 50)
    
    examples = {
        "Simple Document": '''
# Simple ReportLab PDF
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

c = canvas.Canvas("simple_report.pdf", pagesize=letter)
c.drawString(100, 750, "Business Report")
c.drawString(100, 720, "Generated with ReportLab")
c.drawString(100, 690, "Date: 2025-06-28")
c.save()
print("Simple PDF created: simple_report.pdf")
''',
        
        "Professional Document": '''
# Professional ReportLab document with styles
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter

doc = SimpleDocTemplate("business_report.pdf", pagesize=letter)
styles = getSampleStyleSheet()
story = []

# Add title
title = Paragraph("Business Analytics Report", styles['Title'])
story.append(title)
story.append(Spacer(1, 12))

# Add content
content = Paragraph("This is a professional business report generated using ReportLab.", styles['Normal'])
story.append(content)

doc.build(story)
print("Professional PDF created: business_report.pdf")
''',
        
        "Data Table": '''
# ReportLab with data tables
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter

doc = SimpleDocTemplate("data_report.pdf", pagesize=letter)

# Sample data
data = [
    ['Product', 'Sales', 'Profit'],
    ['Product A', '$1,200', '$300'],
    ['Product B', '$2,400', '$600'],
    ['Product C', '$1,800', '$450']
]

table = Table(data)
table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('FONTSIZE', (0, 0), (-1, 0), 14),
    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black)
]))

doc.build([table])
print("Data table PDF created: data_report.pdf")
'''
    }
    
    for title, code in examples.items():
        print(f"\n**{title}:**")
        print("```reportlab")
        print(code.strip())
        print("```")

if __name__ == "__main__":
    print("ReportLab Functionality Test Suite")
    print("=" * 60)
    
    # Test ReportLab availability
    reportlab_available = test_reportlab_availability()
    
    if reportlab_available:
        # Test basic functionality
        test_basic_pdf_generation()
        
        # Show sample code
        create_sample_reportlab_code()
        
        print("\n🎯 Testing Instructions:")
        print("=" * 50)
        print("1. Restart your Flask app: python main.py")
        print("2. In the chat, try these ReportLab examples:")
        print("3. Use ```reportlab code blocks for PDF generation")
        print("4. Click the play button (▶️) to execute")
        print("5. Check /static/outputs/documents/ for generated PDFs")
        
        print("\n✅ ReportLab Integration Benefits:")
        print("- No external LaTeX installation required")
        print("- Pure Python PDF generation")
        print("- Professional document layouts")
        print("- Charts, tables, and graphics support")
        print("- Much faster than LaTeX compilation")
        
    else:
        print("\n❌ ReportLab Installation Required:")
        print("Run: pip install reportlab==4.0.8")
