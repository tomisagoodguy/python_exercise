'''
5	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，將此數反轉順序輸出 (利用 % 與 // 處理)
'''
import os
os.system("cls")

a = int(input('輸入一個正整數 '))

while a != 0:
    print(a % 10, end ='')
    a //= 10    #(a = a//10)