QR Attendance System

Overview
A Python-based QR Code Attendance System using OpenCV.

Features
- Generate QR codes for students
- Scan QR codes using webcam
- Mark attendance with timestamp
- Prevent duplicate entries
- Sound + visual feedback

Tech Stack
- Python
- OpenCV
- Pandas
- QRCode

Project Structure
- src/ → main code
- data/ → student data
- qr_codes/ → generated QR
- attendance/ → attendance logs

How to Run
1. Install dependencies
2. Run:
   ```bash
   python src/generate_qr.py
   python src/scan_qr.py
