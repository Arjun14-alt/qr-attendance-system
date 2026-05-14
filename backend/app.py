from flask import Flask, request, jsonify
import os

from generate_qr import generate_qr_for_student
from attendance import mark_attendance, get_attendance
from student_manager import add_student, get_students

app = Flask(__name__)

# ================= HOME =================
@app.route("/")
def home():
    return "QR Attendance System Running 🚀"


# ================= ADD STUDENT =================
@app.route("/add_student", methods=["POST"])
def add_student_route():
    try:
        data = request.json
        name = data.get("name")

        if not name:
            return jsonify({"error": "name required"}), 400

        student = add_student(name)
        qr_path = generate_qr_for_student(student)

        return jsonify({
            "student": student,
            "qr_path": qr_path
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ================= GET STUDENTS =================
@app.route("/students")
def students_route():
    return jsonify(get_students())


# ================= SCAN QR =================
@app.route("/scan", methods=["POST"])
def scan_route():
    try:
        data = request.json
        qr_data = data.get("qr_data")

        if not qr_data:
            return jsonify({"error": "qr_data required"}), 400

        result = mark_attendance(qr_data)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ================= ATTENDANCE =================
@app.route("/attendance")
def attendance_route():
    return jsonify(get_attendance())


# ================= RENDER ENTRY =================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)