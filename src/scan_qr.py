def scan_qr(qr_data):
    """
    QR format: id|name
    """

    try:
        student_id, name = qr_data.split("|")
        return {
            "id": student_id.strip(),
            "name": name.strip()
        }

    except:
        return {
            "id": None,
            "name": None,
            "error": "Invalid QR format"
        }