
# โปรแกรมสร้างบัตรนักศึกษาจากข้อมูลดิบ

# รับข้อมูลจากผู้ใช้
raw_name = input("กรอกชื่อ-นามสกุล: ")
student_id = input("กรอกรหัสนักศึกษา: ")

# ทำความสะอาดชื่อ ลบช่องว่างที่เกินออก
name = " ".join(raw_name.split())

# ทำให้ตัวอักษรแรกของแต่ละคำเป็นตัวพิมพ์ใหญ่
name = name.title()

# ตรวจสอบรหัสนักศึกษาว่าเป็นตัวเลข 9 หลักหรือไม่
check = student_id.isdigit() and len(student_id) == 9

# ตัดช่วงรหัสนักศึกษา
year = student_id[0:2]       # ปีการศึกษา
branch = student_id[2:4]     # รหัสสาขา
number = student_id[4:9]      # ลำดับที่

# สร้างชื่อผู้ใช้ โดยใช้ชื่อและลำดับที่
username = name.split()[0].lower() + number

# สร้างอีเมลนักศึกษา
email = username + "@student.ac.th"

# สร้างรหัสผ่านจากรหัสนักศึกษา
password = student_id

# แสดงผลข้อมูลบัตรนักศึกษา
print("\n===== บัตรนักศึกษา =====")
print(f"ชื่อ-นามสกุล : {name}")
print(f"รหัสนักศึกษา : {student_id}")
print(f"ปีการศึกษา   : 25{year}")
print(f"รหัสสาขา     : {branch}")
print(f"ลำดับที่     : {number}")

# แสดงข้อมูลบัญชีผู้ใช้
print("\n===== ข้อมูลบัญชี =====")
print(f"Username : {username}")
print(f"Email    : {email}")
print(f"Password : {password}")

# แสดงผลการตรวจสอบรหัส
print("\nรหัสนักศึกษาถูกต้องหรือไม่:", check)
