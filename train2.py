import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

def train():
    global model
    # Đọc dữ liệu từ tệp CSV
    data = pd.read_csv('Student_Performance.csv')

    # Chọn features và target
    X = data[['Hours Studied', 'Previous Scores', 'Extracurricular Activities',
        'Sleep Hours', 'Sample Question Papers Practiced']]
    y = data['Performance Index']

    # Chia dữ liệu thành tập train và tập test
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Tạo một mô hình hồi quy tuyến tính
    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(5,)),  # Số cột đầu vào
        tf.keras.layers.Dense(1)  # Một tầng ẩn với một đầu ra
    ])

    # Biên dịch mô hình
    model.compile(optimizer='adam', loss='mse')  # Sử dụng hàm mất mát Mean Squared Error

    # train
    model.fit(X_train, y_train, epochs=1, batch_size=32, verbose=2)

    # Đánh giá mô hình trên tập test
    loss = model.evaluate(X_test, y_test)
    print("Mất mát trên tập kiểm tra:", loss)



