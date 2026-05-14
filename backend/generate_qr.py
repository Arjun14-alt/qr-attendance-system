import qrcode
import os

QR_FOLDER = "qr_codes"
os.makedirs(QR_FOLDER, exist_ok=True)

def generate_qr_for_student(student):
    data = f'{student["id"]}|{student["name"]}'

    path = os.path.join(QR_FOLDER, f'{student["id"]}.png')

    qr = qrcode.make(data)
    qr.save(path)

    return path