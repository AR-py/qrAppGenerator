# ================================================================================================================ 
# ©️AR
import qrcode
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image

w = Tk()
w.geometry('300x300')
w.configure(bg= 'black')
w.iconbitmap('icon.ico')
w.title('QrCode - AR')
w.resizable(False, False)

lb = Label(w, text= 'QR Data:', font=("System", 8))
lb.configure(bg='black', foreground='white')
lb.pack()

txt1 = Entry(w, width=20, font=("System", 8))
txt1.pack()
txt1.focus()

def qrmake():
    qr = qrcode.make(txt1.get())
    qr.save('qrcode.png', scale = 8)

    for widget in w.winfo_children():
        widget.destroy()
    w.geometry('300x300')
    w.configure(bg= 'black')

    global img

    path = 'qrcode.png'
    img = img = ImageTk.PhotoImage(Image.open(path))

    panel = tk.Label(w, image = img)
    panel.pack()

btn = Button(w, text= 'Submit', command= qrmake, font=("Terminal", 11))
btn.place(x=131, y=60)

w.mainloop()


# ©️AR
# ================================================================================================================ 