'''
7	(1) 請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數n (n < 10)，顯示 n*n乘法表。
    (2)每項運算式格式化排列整齊，每個運算子與運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，
皆靠左對齊不跳行。
'''
import os
os.system("cls")

n = int(input('請輸入小於10的整數：'))

if n < 10:

    for i in range (1, n+1):
        for j in range(1, n+1):
            # print('%d*%-d=%2d '%(j,i,j*i),end='')
            print(f"{j}*{i}={j*i:2}",end=' ')
        print()
else:
    print("輸入值大於或等於10")