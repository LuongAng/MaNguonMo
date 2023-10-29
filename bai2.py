import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
#img = cv2.imread('pic1.png')
#rows, cols = img.shape[:2]
#kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
#kernel_3x3 = np.ones((3,3), np.float32) / 9.0
#kernel_5x5 = np.ones((5,5), np.float32) / 25.0
#cv2.imshow('Original', img)
#output = cv2.filter2D(img, -1, kernel_identity)
#cv2.imshow('Identity filter', output)
#output = cv2.filter2D(img, -5, kernel_3x3)
#cv2.imshow('3x3 filter', output)
#output = cv2.filter2D(img, -1, kernel_5x5)
#cv2.imshow('5x5 filter', output)
#cv2.waitKey(0)

# Khởi tạo biến toàn cục để lưu trữ tọa độ của vùng chọn
start_x, start_y, end_x, end_y = -1, -1, -1, -1
is_drawing = False
selected_region = None
editing_completed = False
def select_region(event, x, y, flags, param):
    global start_x, start_y, end_x, end_y, is_drawing, img, selected_region

    if not editing_completed:
        if event == cv2.EVENT_LBUTTONDOWN:
            start_x, start_y = x, y
            is_drawing = True
        elif event == cv2.EVENT_MOUSEMOVE:
            if is_drawing:
                end_x, end_y = x, y
        elif event == cv2.EVENT_LBUTTONUP:
            is_drawing = False
            end_x, end_y = x, y

            # Vẽ hình chữ nhật để xác định vùng đã chọn
            cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 255, 0), 2)

            # Lưu vùng đã chọn
            selected_region = img[start_y:end_y, start_x:end_x]

def open_image():
    global img, selected_region, editing_completed
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif *.tif")])
    if file_path:
        img = cv2.imread(file_path)
        if img is not None:
            cv2.namedWindow('Portrait')
            cv2.setMouseCallback('Portrait', select_region)
            selected_region = None
            editing_completed = False
            cv2.imshow('Portrait', img)

#Ham lam mo anh
def on_ok_button_click():
    global img, selected_region, editing_completed
    if selected_region is not None:
        # Áp dụng bộ lọc trung bình để làm mịn vùng đã chọn
        kernel = np.ones((5, 5), np.float32) / 25.0
        smoothed_region = cv2.filter2D(selected_region, -1, kernel)
        img[start_y:end_y, start_x:end_x] = smoothed_region

        # Gán vùng đã làm mịn trở lại vào ảnh gốc
        editing_completed = True

        # Cập nhật hiển thị
        cv2.imshow('Portrait', img)

def on_confirm_button_click():
    global img, editing_completed
    if editing_completed:
        # Ẩn viền xanh bằng cách vẽ lại hình chữ nhật màu nền (đặt độ dày thành -1)
        cv2.rectangle(img, (start_x, start_y), (end_x, end_y), (0, 0, 0), -1)
        editing_completed = False
        

