import os
import sys
import subprocess

# Automatically verify and install dependency if missing
try:
    from pypdf import PdfReader
except ImportError:
    print("[INFO] Dependency 'pypdf' not found. Installing now...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf"])
    from pypdf import PdfReader

def process_single_pdf(pdf_filename):
    """Reads a specific PDF file and generates its corresponding HTML file."""
    if not os.path.exists(pdf_filename):
        print(f"[ERROR] Source file '{pdf_filename}' not found.\n")
        return False

    # Define the output name based on the original file name
    base_name = os.path.splitext(pdf_filename)[0]
    output_filename = f"{base_name}_website.html"

    print(f"[PROCESSING] Reading '{pdf_filename}'...")
    try:
        reader = PdfReader(pdf_filename)
        
        # Initialize a clean, responsive HTML5 layout structure
        html_content = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
        html_content += "    <meta charset=\"UTF-8\">\n"
        html_content += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
        html_content += f"    <title>Converted Document - {pdf_filename}</title>\n"
        html_content += "    <style>body { font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; background: #fafafa; color: #333; } p { background: #fff; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px; white-space: pre-wrap; }</style>\n"
        html_content += "</head>\n<body>\n"

        # Extract text page by page
        for page in reader.pages:
            extracted_text = page.extract_text() or ""
            if extracted_text.strip():
                html_content += f"    <p>{extracted_text}</p>\n"

        html_content += "</body>\n</html>"

        # Save the generated website
        with open(output_filename, "w", encoding="utf-8") as f:
            f.write(html_content)
            
        print(f"[SUCCESS] Website Created: '{output_filename}'\n")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to convert '{pdf_filename}'. Reason: {e}\n")
        return False

def batch_convert_all_pdfs():
    """Scans the current folder and converts every PDF file it finds."""
    print("[BATCH] Scanning folder for PDF files...")
    
    # List all files in the current working directory ending with .pdf
    pdf_files = [f for f in os.listdir('.') if f.lower().endswith('.pdf')]

    if not pdf_files:
        print("[INFO] No PDF files found in the current folder.")
        print("Please add some PDF files here and run the tool again.\n")
        return

    print(f"[INFO] Found {len(pdf_files)} PDF file(s) to convert.\n")
    success_count = 0

    for pdf in pdf_files:
        if process_single_pdf(pdf):
            success_count += 1

    print(f"=== Batch Processing Finished ===")
    print(f"Successfully converted {success_count} out of {len(pdf_files)} files.\n")

if __name__ == "__main__":
    print("Welcome to the Advanced PDF to HTML Converter")
    print("=" * 45)
    print("Options:")
    print("1. Type a specific file name (e.g., document.pdf)")
    print("2. Leave it blank and press Enter to convert ALL PDFs in this folder\n")
    
    user_input = input("Enter PDF file name (or press Enter for batch mode): ").strip()
    print("-" * 45)

    if user_input:
        # If user typed something, ensure it ends with .pdf extension
        if not user_input.lower().endswith('.pdf'):
            user_input += '.pdf'
        process_single_pdf(user_input)
    else:
        # Run batch conversion mode
        batch_convert_all_pdfs()
