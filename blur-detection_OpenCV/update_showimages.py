import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os
def show_image(file_path):
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)

        image_label.config(image=photo)
        image_label.image = photo
root = tk.Tk()
root.title("Image Blurriness Checker")

label1 = tk.Label(root, text="Select an image:")
label1.pack()

entry_path = tk.Entry(root)
entry_path.pack()

browse_button = tk.Button(root, text="Browse", command=browse_image)
browse_button.pack()

check_button = tk.Button(root, text="Check Blurriness", command=check_blurriness, state=tk.DISABLED)
check_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

image_label = tk.Label(root)
image_label.pack()

threshold = 500.0

root.mainloop()
