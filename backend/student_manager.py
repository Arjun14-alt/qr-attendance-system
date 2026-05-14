import csv
import os

FILE = "students.csv"

def get_students():
    if not os.path.exists(FILE):
        return []

    students = []
    with open(FILE, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            if len(row) == 2:
                students.append({"id": row[0], "name": row[1]})
    return students


def add_student(name):
    students = get_students()

    new_id = str(100 + len(students) + 1)

    with open(FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_id, name])

    return {"id": new_id, "name": name}