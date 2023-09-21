#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
n = int(input("Nhập số ẩn: "))
m=n

# Khởi tạo ma trận hệ số A và vector vế phải b
A = np.zeros((m, n))
B = np.zeros(n)
C = np.column_stack((A, B))
# Nhập ma trận hệ số A từ người dùng
print("Nhập ma trận hệ số A:")
for i in range(m):
    for j in range(n):
        A[i][j] = float(input(f"A[{i + 1}][{j + 1}]: "))

# Nhập vector vế phải b từ người dùng
print("Nhập vector vế phải b:")
for i in range(m):
    B[i] = float(input(f"b[{i + 1}]: "))
rankA=(np.linalg.matrix_rank(A))
rankC=(np.linalg.matrix_rank(C))    
try:
  A1= np.linalg.inv(A) # tạo ma trận nghich đảo
  X = np.dot(A1,B)
  print("Hệ phương trình có nghiệm duy nhất:",X)
except np.linalg.LinAlgError as e:
    if "Singular matrix" in str(e):
        print("Hệ phương trình có vô số nghiệm hoặc không có nghiệm.")
    else:
        print(f"Lỗi: {str(e)}")
except Exception as e:
    print(f"Lỗi: {str(e)}")
