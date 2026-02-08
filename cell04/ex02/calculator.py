# รับค่าตัวเลขตัวแรกจากผู้ใช้ และแปลงเป็นจำนวนเต็ม (int)
num1 = int(input("Give me the first number: "))
num2 = int(input("Give me the second number: "))
print('Thank You')
# แสดงผลการบวกของ num1 และ num2
print(f"{num1} + {num2} = {num1 + num2}")

# แสดงผลการลบของ num1 และ num2
print(f"{num1} - {num2} = {num1 - num2}")

	# คำนวณการหารและเก็บไว้ในตัวแปร div
div = num1 / num2

# ตรวจสอบว่าได้ผลหารออกมาเป็นจำนวนเต็มหรือไม่ (ไม่มีเศษ)
if div == int(div):
    # ถ้าใช่ แสดงผลลัพธ์เป็นจำนวนเต็ม
    print(f"{num1} / {num2} = {int(num1 / num2)}")
else:
    # ถ้าไม่ใช่ แสดงผลลัพธ์ที่มีทศนิยม
    print(f"{num1} / {num2} = {div}")

# แสดงผลการคูณของ num1 และ num2
print(f"{num1} * {num2} = {num1 * num2}")
