from flask import Flask, request, jsonify
import os

from src.generate_qr import generate_qr
from src.scan_qr import scan_qr
from src.attendance import mark_attendance, get_attendance

app = Flask(__name__)

# =========================
# HOME
# =========================
@app.route("/")
def home():
    return "QR Attendance System Running 🚀"

# =========================
# GENERATE QR FOR STUDENT
# expects: { "student_id": "104" }
# =========================
@app.route("/generate_qr", methods=["POST"])
def generate_qr_route():
    try:
        data = request.json
        student_id = data.get("student_id")

        if not student_id:
            return jsonify({"error": "student_id required"}), 400

        qr_path = generate_qr(student_id)

        if not qr_path:
            return jsonify({"error": "Student not found in CSV"}), 404

        return jsonify({
            "message": "QR generated successfully",
            "student_id": student_id,
            "qr_path": qr_path
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# SCAN QR + MARK ATTENDANCE
# expects: { "qr_data": "104|Arjun" }
# =========================
@app.route("/scan_qr", methods=["POST"])
def scan_qr_route():
    try:
        data = request.json
        qr_data = data.get("qr_data")

        if not qr_data:
            return jsonify({"error": "qr_data required"}), 400

        # decode QR
        student = scan_qr(qr_data)

        # mark attendance
        result = mark_attendance(student)

        return jsonify(result)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# GET ATTENDANCE RECORDS
# =========================
@app.route("/attendance", methods=["GET"])
def attendance_route():
    try:
        data = get_attendance()
        return jsonify(data)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# =========================
# RENDER ENTRY POINT
# =========================
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)