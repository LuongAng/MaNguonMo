#buoihocso6
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import filedialog
from tkinter import Label, Canvas, Button, ttk
from PIL import Image,ImageTk

#chọn ảnh
def image():
    global file_path
    file_path = filedialog.askopenfilename()
    if file_path:
        img = Image.open(file_path)
        img = ImageTk.PhotoImage(img)
        anhgoc = tk.Toplevel()
        anh_goc = tk.Label(anhgoc, image = img)
        anh_goc.pack()
        anhgoc.mainloop()

#1 nửa ảnh
def Haft():
    haft_img = cv2.imread(file_path)
    h, w = haft_img.shape[:2]
    half_width = w // 2
    haft = haft_img[:, :half_width]
    cv2.imshow('Haft_image', haft)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


size_x = tk.StringVar()
size_y = tk.StringVar()
angle = tk.StringVar()
#chỉnh cỡ ảnh
def resize():
    imgresize = cv2.imread(file_path)
    X = int(size_x.get())
    Y = int(size_y.get())
    imgre = cv2.resize(imgresize, (X, Y))
    cv2.imshow('Resize_image', imgre)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#xoay
def rotation():
    rtt_img = cv2.imread(file_path)
    A = int(angle.get())
    height, width = rtt_img.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), A, 1)
    rotated_image = cv2.warpAffine(rtt_img, rotation_matrix, (width, height))
    cv2.imshow("Rotation image", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
