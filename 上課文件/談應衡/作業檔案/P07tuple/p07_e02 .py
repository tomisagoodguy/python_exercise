'''
2.	輸入並建立兩個數組，輸入-9999結束，將此兩數組合併並從小到大排序，顯示排序前的數組和排序後的串列。
'''
# '''
# 建立兩個數組
tup1 = ()
tup2 = ()
print("Creat tuple1:")   #建立第一個數組內容
while True:
    num = int(input("number:"))
    if num == -9999:
        break
    else:
        tup1 += (num,)

print("Creat tuple2:")   #建立第一個數組內容
while True:
    num = int(input("number:"))
    if num == -9999:
        break
    else:
        tup1 += (num,)

tup = tup1 + tup2   #將兩數組合併

print ("Combined tuple before sorting:",tup) #輸出排序前數組

lst = list(tup)     #將數組轉換成串列
lst = sorted(lst)   #將串列排序
print("Combined list after sorting:",lst) #輸出排序後串列
# '''
'''
import os
os.system('cls')
def inpTup(tup):
    i = 1
    while True:
        num = int(input(f"number{i}:"))
        if num == -9999:
            break
        else:
            tup += (num,)
            i += 1
    return tup
def main():
    tup1 = ()
    tup2 = ()

    print("Creat tuple1:")   #建立第一個數組內容
    tup1 = inpTup(tup1)

    print("Creat tuple2:")   #建立第二個數組內容
    tup2 = inpTup(tup2)

    tup = tup1 + tup2   #將兩數組合併

    print ("Combined tuple before sorting:",tup) #輸出排序前數組

    lst = list(tup)     #將數組轉換成串列
    lst = sorted(lst)   #將串列排序
    print("Combined list after sorting:",lst) #輸出排序後串列
    
    pass

main()

'''