#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
n=int(input("Nhập hệ phương trình:"))
A=np.zeros((n,n),dtype=int)
B=np.zeros((n,1),dtype=int)
for i in range(1,n):
  for j in range(1,n):
    a=int(input(f"A[{i}][{j}])="))
    a=A[i][j]

for i in range(1,n):
  for j in range(1,n):
    b=int(input(f"B[{i}][{j}])="))
    b=B[i][j]
A1  = np.linalg.inv(A) # tạo ma trận nghich đảo
print(A)
print(B)
print(A1)
X = np.dot(A1,B)
print('Nghiem cua he:',X)
print('lam thu')
print('aaaaaaaaaaaaaaaaaaaaaaaa')
print('anh luong dep trai')    
