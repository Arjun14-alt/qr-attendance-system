import qrcode
import pandas as pd
import os

# Load student data
data = pd.read_csv("data/students.csv")

# Clean column names (removes spaces + makes lowercase)
data.columns = data.columns.str.strip().str.lower()

# Check if required columns exist
if 'id' not in data.columns or 'name' not in data.columns:
    print("Error: CSV must contain 'id' and 'name' columns")
    print("Found columns:", data.columns)
    exit()

# Output folder
output_folder = "qr_codes"
os.makedirs(output_folder, exist_ok=True)

for index, row in data.iterrows():
    student_id = row['id']
    name = row['name']

    qr_data = f"{student_id},{name}"

    qr = qrcode.make(qr_data)

    file_path = os.path.join(output_folder, f"{name}.png")
    qr.save(file_path)

    print(f"QR created for {name}")

print("All QR codes generated!") 
