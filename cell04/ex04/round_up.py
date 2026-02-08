import math
# นำเข้าโมดูล math เพื่อใช้ฟังก์ชันคณิตศาสตร์ เช่น math.ceil()

num = float(input("Give me a number: "))
# รับค่าตัวเลขจากผู้ใช้ (สามารถเป็นทศนิยมได้) และแปลงเป็นชนิด float

print(f"{(math.ceil(num))}")
# ใช้ math.ceil() เพื่อปัดค่าทศนิยมของ num "ขึ้น" ไปยังจำนวนเต็มถัดไป
# จากนั้นแสดงผลลัพธ์ด้วย f-string
