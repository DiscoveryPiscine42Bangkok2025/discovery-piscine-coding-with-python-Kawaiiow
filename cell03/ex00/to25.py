# รับค่าจาก terminal แล้วทำการแปลงข้อมูลจาก ตัวอักษร -> ตัวเลข จากนั้นทำการเก็บไว้ในตัวแปรชื่อว่า value
value = int(input())

# หากตัวเลขที่ใส่เข้ามามีค่ามากกว่า 25: ให้แสดงผลคำว่า "Error"
if value > 25:
	print("Error")

# หากตัวเลขที่ใส่เข้ามามีค่าน้อยกว่า 25: ให้วนซ้ำแสดงผลตั้งแต่ค่า value จนถึง 25 ในรูปแบบ
# "Inside the loop, my variable is {ค่าปัจจุบัน}"
else:
	for num in range(value, 26):
		print(f"Inside the loop, my variable is {num}")