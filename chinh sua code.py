import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk, filedialog

# Initialize global variables
img = None
current_intensity = 1.0  # Initial intensity

# Function to load image
def load_image():
    global img
    file_path = filedialog.askopenfilename()  # Open a file dialog to choose the image
    if file_path:
        img = cv2.imread(file_path)
        cv2.imshow('Original', img)

# Function to apply effect
def apply_effect():
    global img
    choice = effect_choice.get()
    if choice in kernels and img is not None:
        kernel = kernels[choice] * current_intensity
        output = cv2.filter2D(img, -1, kernel)
        cv2.imshow('Selected Effect', output)
    else:
        print("Invalid choice or no image loaded.")

# Function to increase intensity
def increase_intensity():
    global current_intensity
    current_intensity += 0.1
    apply_effect()

# Function to decrease intensity
def decrease_intensity():
    global current_intensity
    current_intensity -= 0.1
    if current_intensity < 0.1:
        current_intensity = 0.1
    apply_effect()

# Define the kernels
kernels = {
    '1-Sharp': np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]]),
    '2-Excession Sharp': np.array([[1, 1, 1], [1, -7, 1], [1, 1, 1]]),
    '3-': np.array([[-1, -1, -1, -1, -1],
                   [-1, 2, 2, 2, -1],
                   [-1, 2, 8, 2, -1],
                   [-1, 2, 2, 2, -1],
                   [-1, -1, -1, -1, -1]]) / 8.0
}

# Create the main window
window = tk.Tk()
window.title("Image Effects")

# Load Image Button
load_button = ttk.Button(window, text="Load Image", command=load_image)
load_button.pack()

# Dropdown for choosing effect
effect_choice = tk.StringVar()
effect_choice.set("1-sharpen")
effect_label = ttk.Label(window, text="Choose an effect:")
effect_label.pack()
effect_menu = ttk.OptionMenu(window, effect_choice, "1-sharpen", "1-sharpen", "2-excession sharp", "3-")
effect_menu.pack()

# Intensity Buttons
intensity_label = ttk.Label(window, text="Intensity:")
intensity_label.pack()
increase_button = ttk.Button(window, text="Increase", command=increase_intensity)
increase_button.pack()
decrease_button = ttk.Button(window, text="Decrease", command=decrease_intensity)
decrease_button.pack()

# Apply Effect Button
apply_button = ttk.Button(window, text="Apply Effect", command=apply_effect)
apply_button.pack()

window.mainloop()