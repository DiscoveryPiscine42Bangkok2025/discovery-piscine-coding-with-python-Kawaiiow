# รับอายุจากผู้ใช้ โดยแปลงค่าที่รับมา (string) ให้เป็นจำนวนเต็ม (int)
age = int(input("Please tell me your age: "))

# แสดงข้อความว่า "คุณมีอายุเท่าไหร่ในปัจจุบัน"
print(f"You are currently {age} years old.")

# กำหนดตัวแปร add เพื่อใช้เพิ่มจำนวนปี เริ่มต้นที่ 10
add = 10

# ใช้ลูป while เพื่อทำซ้ำตราบใดที่ add มีค่าน้อยกว่าหรือเท่ากับ 30
while (add <= 30):
    # แสดงข้อความว่าในอีก add ปี อายุจะเท่ากับ age + add
    print(f"In {add} years, you'll be {age + add} years old.")
    
    # เพิ่มค่า add ทีละ 10 ทุกครั้งที่ลูปทำงาน
    add += 10
