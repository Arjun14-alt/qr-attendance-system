from flask import Flask, request, jsonify
from flask_cors import CORS

from src.generate_qr import generate_qr_for_student
from src.attendance import mark_attendance, get_attendance
from src.student_manager import add_student, get_students

app = Flask(__name__)
CORS(app)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return "QR Attendance System Running 🚀"


# ---------------- ADD STUDENT ----------------
@app.route("/add_student", methods=["POST"])
def add_student_route():
    data = request.json
    name = data.get("name")

    if not name:
        return jsonify({"error": "name required"}), 400

    student = add_student(name)
    qr_path = generate_qr_for_student(student)

    return jsonify({
        "student": student,
        "qr": qr_path
    })


# ---------------- GET STUDENTS ----------------
@app.route("/students")
def students():
    return jsonify(get_students())


# ---------------- MARK ATTENDANCE ----------------
@app.route("/scan", methods=["POST"])
def scan():
    data = request.json
    qr_data = data.get("qr_data")

    if not qr_data:
        return jsonify({"error": "qr_data missing"}), 400

    result = mark_attendance(qr_data)

    return jsonify(result)


# ---------------- ATTENDANCE RECORDS ----------------
@app.route("/attendance")
def attendance():
    return jsonify(get_attendance())


if __name__ == "__main__":
    app.run()