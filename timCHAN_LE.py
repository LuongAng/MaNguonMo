n = int(input("Insert the value of list: "))
list = []
listChan=[]
listLe=[]

def hamNhap(n,list):
    n0=0
    while n>0:
        n0+=1
        n1= int(input("Insert the {0}st number: ".format(n0)))
        list.append(n1)
        n-=1
def timChan(listChan,list):
    for x1 in list:
        if(x1%2==0):
            listChan.append(x1)
            ddc=len(listChan)
    listChan.sort()
    inC = print("the even: ", listChan)
    return ddc
def timLe(listLe,list):
    for x2 in list:
        if(x2%2!=0):
            listLe.append(x2)
            ddl= len(listLe)
    listLe.sort()
    inL=print("the odd: ",listLe)
    return ddl

hamNhap(n, list)
print("the number of the even number is: ", timChan(listChan,list))
print("the number of the odd number is: ", timLe(listLe,list))


