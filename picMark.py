import tkinter as tk
from tkinter import filedialog
import customtkinter
from PIL import Image, ImageTk

customtkinter.set_appearance_mode("dark") 
customtkinter.set_default_color_theme("blue")  

class PicMark():
    def __init__(self):
        self.window = customtkinter.CTk()  
        self.window.config(padx=30, pady=30)
        self.window.title("PicMark")

        self.canvas = tk.Canvas(highlightthickness=0)
        self.canvas.bind("<Button-1>", self.click)

        logo = customtkinter.CTkImage(dark_image=Image.open("logo.png"), size=(350, 100))
        logo_label = customtkinter.CTkLabel(master=self.window, text="", image=logo)
        logo_label.grid(row=0, column=1)

        back_btn = customtkinter.CTkButton(master=self.window, text="Select Background", command=self.background, font=("TkDefaultFont", 15, "bold"))
        back_btn.grid(column=1, row=2, pady=10)

        water_btn = customtkinter.CTkButton(master=self.window, text="Select Watermark", command=self.watermark, font=("TkDefaultFont", 15, "bold"))
        water_btn.grid(column=1, row=3, pady=10)

        save_btn = customtkinter.CTkButton(master=self.window, text="Save", command=self.save, font=("TkDefaultFont", 15, "bold"))
        save_btn.grid(column=1, row=4, pady=10)

        self.background_img = None 
        self.watermark_img = None
        self.photo = None 
        self.x = None 
        self.y = None 
        self.im1 = None 
        self.im2 = None 

    def background(self):
            filename = filedialog.askopenfilename()
            self.background_img = Image.open(filename)

            scale_image = self.background_img.resize((self.background_img.width // 2, self.background_img.height // 2))
            self.photo = ImageTk.PhotoImage(scale_image)

            self.canvas.config(width=scale_image.width, height=scale_image.height)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
            self.canvas.grid(column=1, row=1, pady=10)

    def watermark(self):
            filename = filedialog.askopenfilename()
            self.watermark_img = Image.open(filename).convert("RGBA")

    def click(self, event):
        self.x = event.x * 2
        self.y = event.y * 2

        self.im1 = self.background_img.copy()
        self.im2 = self.watermark_img.copy()

        self.im1.paste(self.im2, (self.x, self.y), self.im2)

        scale_image = self.im1.resize((self.im1.width // 2, self.im1.height // 2))
        self.photo = ImageTk.PhotoImage(scale_image)
        
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)
        self.canvas.update()


    def save(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png")
        self.im1.paste(self.im2, (self.x, self.y), self.im2)
        self.im1.save(filename, format="png")

if __name__ == "__main__":
    app = PicMark()
    app.window.mainloop()