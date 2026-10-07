# Advanced PDF → HTML Website Converter 📄➡️🌐

A flexible Python CLI application that reads local PDF documents, extracts their text formatting, and dynamically compiles them into clean, modern, and responsive HTML5 webpages.

---

## How to Use This Project

Follow these steps to download and run the application on your computer:

### 1. Download the Files
* Click the green **"Code"** button at the top of this GitHub page.
* Select **"Download ZIP"** and extract the files into a folder.

### 2. Prepare Your PDF Files
* Copy the PDF files you want to convert and paste them inside the **same folder** as the scripts.

### 3. Open Your Terminal
* **Windows:** Open the folder, hold `Shift`, right-click an empty space, and choose **"Open PowerShell window here"** or **"Open in Terminal"**.
* **Mac / Linux:** Open your Terminal app and use the `cd` command to navigate to the project directory.

### 4. Install Requirements & Run the Tool

#### 🪟 On Windows
```bash
python -m pip install -r requirements.txt
python main.py
```

#### 🍏 On macOS / 🐧 On Linux
```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

### 5. Choose Your Conversion Mode
When the script runs, it will ask you for an input:
* **Single File Mode:** Type the name of a specific file (e.g., `my_document.pdf`) and hit Enter.
* **Batch Mode:** Just press **Enter** without typing anything, and the tool will automatically find and convert **every single PDF file** inside that folder at once!

### Voilá! Website created succefully!

---

## Requirements
* **Python 3.8 or higher** installed on your system.
