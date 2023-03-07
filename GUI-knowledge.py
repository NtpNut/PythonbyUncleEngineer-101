from tkinter import *
from tkinter import ttk, messagebox
import random

# สร้าง GUI
GUI = Tk()
GUI.title("Pafum Today")
GUI.geometry("960x760")


# สร้างฟังก์ชันสำหรับสุ่มภาพและข้อความ
def random_image_text():
    # กำหนด list ของรูปภาพ
    images = ['Layton.png', 'Yulong.png', 'YSL.png','Bleu de CHANEL.png','Ck be.png','Suvage.png']

    # สุ่มรูปภาพจาก list
    selected_image = random.choice(images)

    # สร้างฟังก์ชันสำหรับแสดงข้อความใน messagebox
    def show_message():
        messagebox.showinfo("Pafum Today", "Have a nice day")

    # แสดงภาพ
    image = PhotoImage(file=selected_image)
    label_image.config(image=image)
    label_image.image = image

    # แสดงข้อความ
    GUI.after(100, show_message)


# สร้างปุ่มสำหรับสุ่มภาพและข้อความ
random_button = ttk.Button(GUI, text="Random Pafum", command=random_image_text)
random_button.pack(ipadx=30,ipady=30)


# สร้าง label สำหรับแสดงภาพ
label_image = Label(GUI)
label_image.pack()

GUI.mainloop()
