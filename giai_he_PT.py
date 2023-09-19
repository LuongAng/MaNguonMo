#bài này giải hệ phương trình x+2y=5 và 3x+4y =6
# Yêu cầu hoàn chỉnh lại đoạn code
#để có 1 app giải hệ phương trình có n phương trình n ẩn
import numpy as np
n=int(input("Nhập hệ phương trình:"))
A=np.zeros((n,n),dtype=int)
B=np.zeros((n,n),dtype=int)
C=np.zeros((n,n+1),dtype=int)
for i in range(0,n):
  for j in range(0,n):
    a=int(input(f"A[{i+1}][{j+1}])="))
    a=A[i][j]
for i in range(0,n):
  for j in range(0,1):
    b=int(input(f"B[{i+1}][{j+1}])="))
    b=B[i][j]
for i in range(0,n):
  for j in range(0,n):
    C[i][j]=A[i][j]
for i in range(0,n):
  for j in range(0,n):
    C[i][j]=B[i][0]
try:
  A1= np.linalg.inv(A) # tạo ma trận nghich đảo
  X = np.dot(A1,B)
  print("Hệ phương trình có nghiệm duy nhất:",X)
except:
  rankA=(np.linalg.matrix_rank(A))
  rankC=(np.linalg.matrix_rank(C))
  #rankA1=(np.linalg.matrix_rank(1))
  if(rankA<rankC):
    print("Hệ phương trình vô nghiệm")
  elif (rankA==rankC)and(rankA<n)and(rankC<n):
    print("PHuong trinh vo so nghiem")
