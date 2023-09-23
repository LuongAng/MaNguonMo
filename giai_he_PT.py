import numpy as np
n = int(input("Nhập số ẩn: "))
m=n

# Khởi tạo ma trận hệ số A và vector vế phải b
A = np.zeros((m, n))
B = np.zeros(n)
# Nhập ma trận hệ số A từ người dùng
print("Nhập ma trận hệ số A:")
for i in range(m):
    for j in range(n):
        A[i][j] = float(input(f"A[{i + 1}][{j + 1}]: "))

# Nhập vector vế phải b từ người dùng
print("Nhập vector vế phải b:")
for i in range(m):
    B[i] = float(input(f"b[{i + 1}]: "))

# Tính rank của ma trận hệ số A và ma trận mở rộng [A | B]
rank_A = np.linalg.matrix_rank(A)
rank_AB = np.linalg.matrix_rank(np.column_stack((A, B)))

# Số biến trong hệ phương trình
num_variables = A.shape[1]

if rank_A < rank_AB:
    print("Hệ phương trình không có nghiệm.")
elif rank_A == rank_AB < num_variables:
    print("Hệ phương trình có vô số nghiệm.")
elif rank_A == rank_AB == num_variables:
    try:
        X = np.linalg.solve(A, B)
        print("Hệ phương trình có một nghiệm duy nhất:")
        print(X)
    except np.linalg.LinAlgError as e:
        print("Hệ phương trình không có nghiệm.")
