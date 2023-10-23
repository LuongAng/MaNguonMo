import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import os

def is_valid_image(file_path):
    try:
        image = Image.open(file_path)
        return image.format in ['JPEG', 'PNG']  # Kiểm tra định dạng ảnh
    except:
        return False
def show_image(file_path):
    if file_path:
        image = Image.open(file_path)
        image.thumbnail((400, 400))
        photo = ImageTk.PhotoImage(image)

        image_label.config(image=photo)
        image_label.image = photo

def check_blurriness():
    file_path = entry_path.get()
    if file_path:
        if not is_valid_image(file_path):
            result_label.config(text="Invalid image format. Please choose a JPEG or PNG image.")
        else:
            image = cv2.imread(file_path)
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = variance_of_laplacian(gray)

            if fm > threshold:
                result_label.config(text="Image is Not Blurry (Variance: {:.2f})".format(fm))
            else:
                result_label.config(text="Image is Blurry (Variance: {:.2f})".format(fm))

