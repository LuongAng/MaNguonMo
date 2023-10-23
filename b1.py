# bai 1 nhap 2 so a,b tim tong, hieu tich thuong cua 2 so na
try:
    a = float(input("nhap so a"))
    b= float(input('nhap b:'))
    if b == 0:
        print("vui long kiem tra lai")
    tong = a + b
    hieu = a - b
    tich = a*b
    thuong = a/b
    print('tong = ', a+b)
    print('hieu =',a-b)
    print('tich =',a*b)
    print('thuong = ',a/b)
except ValueError as e:
    print('Lỗi:', e)
except ZeroDivisionError:
    print('Lỗi: Chia cho 0')
except:
    print(' du lieu nhap khong dung')
    print("abc")
finally:
    print('ket thuc chuong trinh!')


