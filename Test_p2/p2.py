# โปรแกรมสร้างบัตรนักศึกษาจากข้อมูลดิบ

# รับข้อมูลบรรทัดเดียว: "ชื่อ นามสกุล รหัสนักศึกษา"
raw = input("กรอก ชื่อ นามสกุล รหัสนักศึกษา (คั่นด้วยช่องว่าง): ")

# แยกทีเดียวด้วย split() (ตัดช่องว่างเกินให้อัตโนมัติ)
parts = raw.split()

# คำสุดท้ายคือรหัสนักศึกษา ที่เหลือข้างหน้าคือชื่อ-นามสกุล
student_id = parts[-1]
name = " ".join(parts[:-1]).title()

# ตรวจสอบรหัสนักศึกษาว่าเป็นตัวเลข 9 หลักหรือไม่
check = student_id.isdigit() and len(student_id) == 9

# ตัดช่วงรหัสนักศึกษา เช่น 684245006
year = student_id[0:2]        # 68  = ปีการศึกษา
status_code = student_id[2]   # 4   = สถานะการเรียน
branch = student_id[3:6]      # 245 = รหัสสาขา
number = student_id[6:9]      # 006 = ลำดับที่

# แปลงรหัสสถานะเป็นข้อความ
status_map = {
    "1": "เอก",
    "2": "โท",
    "3": "พิเศษ",
    "4": "ภาคปกติ",
}
status = status_map.get(status_code, "ไม่ทราบสถานะ")

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
print(f"สถานะการเรียน: {status} ({status_code})")
print(f"รหัสสาขา     : {branch}")
print(f"ลำดับที่     : {number}")

# แสดงข้อมูลบัญชีผู้ใช้
print("\n===== ข้อมูลบัญชี =====")
print(f"Username : {username}")
print(f"Email    : {email}")
print(f"Password : {password}")

# แสดงผลการตรวจสอบรหัส
print("\nรหัสนักศึกษาถูกต้องหรือไม่:", check)