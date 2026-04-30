import cv2
import pandas as pd
import os
from datetime import datetime
import winsound  # for sound (Windows)

cap = cv2.VideoCapture(0)
detector = cv2.QRCodeDetector()

attendance_file = "attendance/attendance.csv"

# Create file if not exists
if not os.path.exists(attendance_file):
    df = pd.DataFrame(columns=["ID", "Name", "Time"])
    df.to_csv(attendance_file, index=False)

marked_names = set(pd.read_csv(attendance_file)["Name"])

last_scanned = ""
display_text = ""

print("Scanning... Press ESC to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    data, bbox, _ = detector.detectAndDecode(frame)

    if data:
        student_id, name = data.split(",")

        if name != last_scanned:  # avoid rapid repeats
            if name not in marked_names:
                now = datetime.now().strftime("%H:%M:%S")

                new_entry = pd.DataFrame([[student_id, name, now]],
                                         columns=["ID", "Name", "Time"])

                new_entry.to_csv(attendance_file, mode='a',
                                 header=False, index=False)

                marked_names.add(name)

                display_text = f"{name} Marked Present"
                print(display_text)

                winsound.Beep(1000, 300)  # sound

            else:
                display_text = f"{name} Already Marked"
                print(display_text)

                winsound.Beep(500, 300)

            last_scanned = name

    # Draw QR box
    if bbox is not None:
        bbox = bbox.astype(int)
        for i in range(len(bbox)):
            pt1 = tuple(bbox[i][0])
            pt2 = tuple(bbox[(i+1) % len(bbox)][0])
            cv2.line(frame, pt1, pt2, (0, 255, 0), 2)

    # Display text on screen
    if display_text:
        cv2.putText(frame, display_text, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)

    cv2.imshow("QR Attendance System", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()