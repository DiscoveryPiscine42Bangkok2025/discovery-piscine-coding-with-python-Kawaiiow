# รับค่าตัวเลขตัวแรกจาก terminal แล้วทำการแปลงข้อมูลจาก ตัวอักษร -> ตัวเลข
num1 = int(input("Enter the first nunber:"))
# รับค่าตัวเลขตัวที่สองจาก terminal แล้วทำการแปลงข้อมูลจาก ตัวอักษร -> ตัวเลข
num2 = int(input("Enter the second nunber:"))

# ทำการแสดงตัวเลขที่เราใส่เข้ามาทั้งสองตัวในรูปแบบ
# "{เลขตัวที่ 1} x {เลขตัวที่ 2} = {เลขตัวที่ 1 คูณเลขตัวที่ 2}"
print(f"{num1} x {num2} = {num1 * num2}")

# หากผลคูณของเลขทั้งสองตัวมากกว่า 0: ให้ทำงานตรงนี้
if num1 * num2 > 0:
	print("The result is positive.")
	
# หากผลคูณของเลขทั้งสองตัวน้อยกว่า 0: ให้ทำงานตรงนี้
elif num1 * num2 < 0:
	print("The result is negative.")

# หากทั้งสองเงื่อนไขไม่เป็นจริง: ให้ทำงานตรงนี้แทน
else:
	print("The result is positive and negative.")
