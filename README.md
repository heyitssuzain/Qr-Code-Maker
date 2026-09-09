# 🚀 Advanced QR Code Generator (Python)

A professional, production-ready Command Line Interface (CLI) tool written in Python to generate unique, high-quality QR codes. It automatically prevents file overwriting by creating unique filenames based on your input text and timestamps.

## ✨ Features

- 🔄 **Smart Unique Naming**: Automatically converts URLs/text into safe filenames and appends a real-time timestamp (`YYYYMMDD_HHMMSS`). Never overwrites your old files!
- 📁 **Automated Organization**: Creates and saves all images inside a dedicated `generated_qrcodes/` folder to keep your root directory clean.
- 🛠️ **High Error Correction (`ERROR_CORRECT_H`)**: Uses the highest standard error correction, keeping the QR code readable even if it is partially damaged or covered.
- 🧼 **Filename Sanitization**: Automatically removes illegal characters (like `/`, `:`, `?`) that operating systems don't allow in file names.

---

## 📋 System Requirements & Dependencies

To run this project, your system needs to meet the following requirements:

### 1. Prerequisites
- **Python:** Version `3.7` or higher installed on your system.

### 2. Python Packages Required
You need to install the following libraries to process and handle the QR image creation:
- **`qrcode`**: The core library used to generate the QR data matrix.
- **`pillow` (PIL)**: Used behind the scenes by the `qrcode` library to process, color, and render the final PNG image.

---

## 🚀 Quick Setup & Installation

Follow these quick steps to get the project running locally on your machine:

### Step 1: Clone the Repository
```bash
git clone https://github.com/heyitssuzain/Qr-Code-Maker.git
cd Qr-Code-Maker
```

### Step 2: Install Dependencies
You can install the required packages directly using `pip`:
```bash
pip install qrcode[pillow]
```
---

## 💻 How To Use

1. Run the Python script in your terminal or command prompt:
   ```bash
   python Advance Qr Code Generator.py
   ```
2. Enter your desired text or URL link when prompted.
3. Check the `generated_qrcodes/` folder in your project directory to view your clean, high-resolution QR code image.

---

## 🛠️ Customization Tip
You can easily customize the color scheme of your QR code by modifying lines inside `qr_generator.py`:
```python
# Change "black" and "white" to any hex color code like "#1A237E" or "#FFFFFF"
img = qr.make_image(fill_color="black", back_color="white")
```
