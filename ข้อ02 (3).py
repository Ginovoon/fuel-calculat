import tkinter as tk

def calculate_fuel_cost():
    # รับค่าจากผู้ใช้
    distance = float(distance_entry.get())
    consumption_rate = float(consumption_entry.get())
    fuel_price = float(fuel_price_entry.get())
    
    # คำนวณค่าน้ำมัน
    fuel_needed = distance / consumption_rate
    fuel_cost = fuel_needed * fuel_price
    
    # แสดงผลลัพธ์
    result_label.config(text=f"ค่าน้ำมันที่ต้องจ่าย: {fuel_cost:.2f} บาท")

# สร้างหน้าต่าง GUI
root = tk.Tk()
root.title("คำนวณค่าน้ำมัน")

# สร้าง Label และ Entry สำหรับรับข้อมูล
distance_label = tk.Label(root, text="ระยะทาง (กิโลเมตร):")
distance_label.pack()
distance_entry = tk.Entry(root)
distance_entry.pack()

consumption_label = tk.Label(root, text="อัตราสิ้นเปลือง (กิโลเมตร/ลิตร):")
consumption_label.pack()
consumption_entry = tk.Entry(root)
consumption_entry.pack()

fuel_price_label = tk.Label(root, text="ราคาน้ำมัน (บาท/ลิตร):")
fuel_price_label.pack()
fuel_price_entry = tk.Entry(root)
fuel_price_entry.pack()

# ปุ่มคำนวณ
calculate_button = tk.Button(root, text="คำนวณ", command=calculate_fuel_cost)
calculate_button.pack()

# แสดงผลลัพธ์
result_label = tk.Label(root, text="")
result_label.pack()

# เริ่มต้น GUI
root.mainloop()
tk.tk