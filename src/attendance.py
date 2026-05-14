import json
import os
from datetime import datetime

DATA_FILE = "attendance.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)


def mark_attendance(student):
    """
    student = {id, name}
    """

    if not student.get("id"):
        return {"error": "Invalid student"}

    with open(DATA_FILE, "r") as f:
        data = json.load(f)

    student_id = student["id"]

    record = {
        "name": student["name"],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    if student_id not in data:
        data[student_id] = []

    data[student_id].append(record)

    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return {
        "status": "marked",
        "student": student,
        "time": record["time"]
    }


def get_attendance():
    with open(DATA_FILE, "r") as f:
        return json.load(f)