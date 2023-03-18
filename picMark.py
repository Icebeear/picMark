import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")  

window = customtkinter.CTk()  
window.config(padx=30, pady=30)
window.title("PicMark")

canvas = tk.Canvas(highlightthickness=0)

logo = customtkinter.CTkImage(dark_image=Image.open("logo.png"), size=(350, 100))
logo_label = customtkinter.CTkLabel(master=window, text="", image=logo)
logo_label.grid(row=0, column=1)


def click(event):
    global photo
    global x 
    global y 
    x = event.x * 2
    y = event.y * 2

    im1 = Image.open(background)
    im2 = Image.open(watermark).convert("RGBA")
    im1.paste(im2, (x, y), im2)

    scale_image = im1.resize((im1.width // 2, im1.height // 2))
    photo = ImageTk.PhotoImage(scale_image)
    
    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    canvas.update()


def background():
    global background
    global photo 

    background = filedialog.askopenfilename()
    img = Image.open(background)
    scale_image = img.resize((img.width // 2, img.height // 2))


    canvas.config(width=scale_image.width, height=scale_image.height)
    canvas.grid(column=1, row=1, pady=10)

    photo = ImageTk.PhotoImage(scale_image)

    canvas.create_image(0, 0, anchor=tk.NW, image=photo)
    

    
def watermark():
    global watermark
    watermark = filedialog.askopenfilename()


def save():
    filename = filedialog.asksaveasfilename(defaultextension=".png")
    im1 = Image.open(background)
    im2 = Image.open(watermark).convert("RGBA")
    im1.paste(im2, (x, y), im2)
    im1.save(filename, format="png")



back_btn = customtkinter.CTkButton(master=window, text="Select Background", command=background, font=("TkDefaultFont", 15, "bold"))
back_btn.grid(column=1, row=2, pady=10)

water_btn = customtkinter.CTkButton(master=window, text="Select Watermark", command=watermark, font=("TkDefaultFont", 15, "bold"))
water_btn.grid(column=1, row=3, pady=10)

save_btn = customtkinter.CTkButton(master=window, text="Save", command=save, font=("TkDefaultFont", 15, "bold"))
save_btn.grid(column=1, row=4, pady=10)

canvas.bind("<Button-1>", click)

window.mainloop()