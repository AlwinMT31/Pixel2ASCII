# 🎨 Pixel2ASCII – Low-Level Image to ASCII Converter in Python

## 📌 Overview

Pixel2ASCII is a Python-based project that converts **24-bit BMP images into ASCII art** by directly reading and processing raw image bytes. The project avoids all image-processing libraries and performs image decoding, resizing, and ASCII rendering entirely at the byte level using core Python constructs.

The generated ASCII art is displayed in the terminal and also saved to a text file for reuse.

---

## 🎯 Key Features

- Supports uncompressed **24-bit BMP images**
- No external libraries used
- Manual BMP header parsing
- Pixel-wise grayscale conversion
- Aspect-ratio preserving image resizing
- Threshold-based ASCII character mapping
- Terminal-based ASCII output
- ASCII output saved to a `.txt` file

---

## 🧠 Implementation Overview

- Reads BMP files in binary mode
- Extracts width, height, and pixel data offset from the BMP header
- Processes pixel data stored in BGR format
- Converts each pixel to grayscale using integer arithmetic
- Maps grayscale values to ASCII characters
- Handles BMP bottom-up pixel storage format
- Outputs ASCII art line by line

---

## 🛠 Technologies Used

- Python 3
- Binary file handling
- Byte-level data manipulation
- Core Python control structures (`while`, `if`, arithmetic operations)

---

⚠️ Precautions

Only 24-bit uncompressed BMP files are supported
Do not use JPG, PNG, or compressed BMP images
Image file must be named exactly image.bmp
Very large images may slow execution or overflow terminal width
Recommended image width: 800–1200 pixels
Use a monospace font for proper ASCII alignment
Ensure the terminal window is wide enough for clean output

📥 Input & 📤 Output
Input
24-bit BMP image (image.bmp)

Output
ASCII art displayed in terminal
ASCII art saved as neymar_ascii.txt
