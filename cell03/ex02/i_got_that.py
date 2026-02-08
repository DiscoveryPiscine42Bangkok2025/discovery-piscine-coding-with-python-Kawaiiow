# รับค่าจาก terminal แล้วเก็บไว้ในตัวแปร msg
msg = input("What you gotta say? : ")

# ทำการวนซ้ำไปเรื่อยๆ แบบไม่สิ้นสุด
while True:
	
	# ถ้าข้อความที่ส่งเข้ามาคือ "STOP": ให้ทำการออกจากการวนซ้ำ
	if msg == "STOP":
		break

	# ถ้าเงื่อนไขไม่เป็นจริง: ให้ทำการรับค่าจาก terminal แล้วเก็บไว้ในตัวแปร msg
	msg = input("I got that! Anything else? : ")