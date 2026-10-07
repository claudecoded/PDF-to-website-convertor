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

def convert_pdf_to_html(pdf_filename="file.pdf", output_filename="pdf_website.html"):
    """Reads a local PDF document and extracts its text contents into a valid HTML5 structure."""
    
    # Check if the source PDF file actually exists to prevent crashes
    if not os.path.exists(pdf_filename):
        print(f"[ERROR] Source file '{pdf_filename}' not found.")
        print(f"Please place a PDF file named '{pdf_filename}' inside this folder and try again.")
        return

    print(f"[PROCESSING] Reading '{pdf_filename}'...")
    reader = PdfReader(pdf_filename)
    
    # Initialize a clean, responsive HTML5 layout structure
    html_content = "<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n"
    html_content += "    <meta charset=\"UTF-8\">\n"
    html_content += "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
    html_content += f"    <title>Converted Document - {pdf_filename}</title>\n"
    html_content += "    <style>body { font-family: sans-serif; line-height: 1.6; padding: 20px; max-width: 800px; margin: 0 auto; background: #fafafa; color: #333; } p { background: #fff; padding: 15px; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); margin-bottom: 15px; white-space: pre-wrap; }</style>\n"
    html_content += "</head>\n<body>\n"

    # Iterate through all available pages and safely append text blocks
    for page in reader.pages:
        extracted_text = page.extract_text() or ""
        # Clean potential empty lines or spaces
        if extracted_text.strip():
            html_content += f"    <p>{extracted_text}</p>\n"

    html_content += "</body>\n</html>"

    # Write the compiled web layout data to the file system
    print(f"[WRITING] Generating website structure into '{output_filename}'...")
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(html_content)
        
    print("Website Created!")

if __name__ == "__main__":
    convert_pdf_to_html()
