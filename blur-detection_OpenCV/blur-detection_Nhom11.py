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
