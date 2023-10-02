import pandas as pd
from numpy import array
import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk

df=pd.read_csv('diemPython.csv',index_col=0,header = 0)
in_data = array(df.iloc[:,:])

tongsv = in_data[:,1]
diemA = in_data[:,3]
diemC = in_data[:,7]
diemB = in_data[:,5]
diemD = in_data[:,9]
diemF = in_data[:,10]
diemAc = in_data[:,2]
diemBc = in_data[:,4]
diemCc = in_data[:,6]
diemDc = in_data[:,8]

tong = np.sum(diemA) + np.sum(diemAc) + np.sum(diemB) + np.sum(diemBc) + np.sum(diemC) + np.sum(diemCc) + np.sum(
    diemD) + np.sum(diemDc)

bdcot=[np.sum(diemAc),np.sum(diemA),np.sum(diemBc),np.sum(diemB),
       np.sum(diemCc),np.sum(diemC),np.sum(diemDc),np.sum(diemD),np.sum(diemF),]
bdten=['A+','A', 'B+', 'B','C+', 'C','D+','D','F']

maxa = diemA.max()
i, =np.where(diemA == maxa)

def thong_ke():

    label = tk.Label(window, text=f"""{in_data}\nTong so sinh vien di thi :\n{np.sum(tongsv)}
    So sv theo tung lop:, {tongsv}
    lop co nhieu diem A nhat la: {in_data[i, 0]} co {maxa} sv dat diem A
    TBC sinh vien dat moi lop: {tong//9}""")
    label.pack()

def bieu_do():

    plt.subplot(2, 2, 1)
    plt.bar(bdten,bdcot)
    plt.xlabel('diem')
    plt.ylabel(' So sv dat diem ')

    label = ['A','B','C','D','F']

    a=(np.sum(diemA)+np.sum(diemAc))/np.sum(tongsv)*100
    b=(np.sum(diemB)+np.sum(diemBc))/np.sum(tongsv)*100
    c=(np.sum(diemC)+np.sum(diemCc))/np.sum(tongsv)*100
    d=(np.sum(diemD)+np.sum(diemDc))/np.sum(tongsv)*100
    f=np.sum(diemF)/np.sum(tongsv)*100
    sizes = [a, b, c, d, f]

    plt.subplot(2, 2, 2)
    plt.pie(sizes, labels=label,autopct= '%1.1f%%')
    plt.title("Biểu đồ phần trăm điểm sinh viên")
    #
    plt.axis('equal')
    plt.tight_layout()
    plt.show()

window = tk.Tk()
window.title("Giao diện đơn giản")

label = tk.Label(window, text="Chào mừng bạn đến với giao diện đơn giản!")
label.pack()

def button_click():
    bieu_do()

def button_click2():
    thong_ke()

button = tk.Button(window, text="biểu đồ", command=button_click)
button.pack()
button2 = tk.Button(window, text="thống kê", command=button_click2)
button2.pack()

window.mainloop()

