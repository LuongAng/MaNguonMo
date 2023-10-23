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

def variance_of_laplacian(image):
    return cv2.Laplacian(image, cv2.CV_64F).var()

def browse_image():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, tk.END)
    entry_path.insert(0, file_path)
    show_image(file_path)
    check_button.config(state=tk.NORMAL)  # Khi đã chọn ảnh, bật nút kiểm tra

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

