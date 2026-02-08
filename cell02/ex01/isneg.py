# รับค่าจาก terminal แล้วทำการแปลงข้อมูลจาก ตัวอักษร -> ตัวเลข
value = int(input())

# ทำการเช็คว่าค่าตัวเลขที่รับเข้ามามีค่ามากกว่า 0 หรือไม่
if value > 0:
	print("This number is positive.")
	
# หากเงื่อนไขแรกไม่เป็นจริง: ทำการเช็คต่อว่าค่าตัวเลขที่รับเข้ามามีค่าน้อยกว่า 0 หรือไม่
elif value < 0:
	print("This number is negative.")

# หากทั้งสองเงื่อนไขไม่เป็นจริง: ให้ทำงานตรงนี้แทน
else:
	print("This number is both positive and negative.")
