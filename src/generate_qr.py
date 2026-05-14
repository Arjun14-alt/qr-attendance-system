import qrcode
import os
import csv

QR_FOLDER = "qr_codes"
STUDENT_FILE = "students.csv"

os.makedirs(QR_FOLDER, exist_ok=True)


def load_students():
    students = []

    with open(STUDENT_FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) >= 2:
                students.append({
                    "id": row[0].strip(),
                    "name": row[1].strip()
                })

    return students


def generate_qr(student_id):
    """
    Generate QR for a specific student ID from CSV
    """

    students = load_students()

    student = next((s for s in students if s["id"] == str(student_id)), None)

    if not student:
        return None

    qr_data = f'{student["id"]}|{student["name"]}'

    file_path = os.path.join(QR_FOLDER, f'{student["id"]}.png')

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img.save(file_path)

    return file_path