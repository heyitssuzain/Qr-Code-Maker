import os
import re
from datetime import datetime
import qrcode
from qrcode.constants import ERROR_CORRECT_H

def slugify(text):
    """
    Converts user input into a safe, clean file name.
    Removes special characters and limits length.
    """
    # Remove URL protocols if present to keep the name clean
    text = re.sub(r'(https?://)?(www\.)?', '', text)
    # Allow only alphanumeric characters and hyphens
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[\s_]+', '_', text)
    return text[:30]  # Limit to 30 characters

def generate_qr():
    print("=" * 50)
    print("      PROFESSIONAL QR CODE GENERATOR v2.0      ")
    print("=" * 50)
    
    # 1. Get User Input
    data = input("\nEnter your text or URL: ").strip()
    if not data:
        print("❌ Error: Input cannot be empty!")
        return

    # 2. Configure Professional QR Code Settings
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECT_H,  # High error correction (allows logo overlay later)
        box_size=10,                        # Size of each box
        border=4,                           # Standard professional white border
    )
    qr.add_data(data)
    qr.make(fit=True)

    # 3. Custom Styling (Change colors easily)
    # You can change 'black' and 'white' to hex codes like '#000000' and '#FFFFFF'
    img = qr.make_image(fill_color="black", back_color="white")

    # 4. Smart Unique Naming Mechanism
    output_dir = "generated_qrcodes"
    os.makedirs(output_dir, exist_ok=True)  # Creates a dedicated folder

    clean_name = slugify(data)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Fallback name if input yields empty slug (e.g., only emojis/special characters)
    if not clean_name:
        clean_name = "qr_code"
        
    filename = f"{clean_name}_{timestamp}.png"
    filepath = os.path.join(output_dir, filename)

    # 5. Save and Display
    img.save(filepath)
    print(f"\n✅ QR Code Successfully Generated!")
    print(f"📁 Saved as: {filepath}")
    print("=" * 50)
    
    img.show()

if __name__ == "__main__":
    generate_qr()
