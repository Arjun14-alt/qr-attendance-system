import qrcode
import os

QR_FOLDER = "qr_codes"


def ensure_folder():
    if not os.path.exists(QR_FOLDER):
        os.makedirs(QR_FOLDER)


def generate_qr_for_student(student):
    ensure_folder()

    data = f'{student["id"]}|{student["name"]}'
    path = os.path.join(QR_FOLDER, f'{student["id"]}.png')

    qr = qrcode.make(data)
    qr.save(path)

    return path