import json
import os
from datetime import datetime

FILE = "attendance.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump({}, f)


def mark_attendance(qr_data):
    try:
        student_id, name = qr_data.split("|")

        with open(FILE, "r") as f:
            data = json.load(f)

        if student_id not in data:
            data[student_id] = []

        data[student_id].append({
            "name": name,
            "time": str(datetime.now())
        })

        with open(FILE, "w") as f:
            json.dump(data, f, indent=4)

        return {
            "status": "marked",
            "student": name
        }

    except:
        return {"error": "invalid qr"}


def get_attendance():
    with open(FILE, "r") as f:
        return json.load(f)