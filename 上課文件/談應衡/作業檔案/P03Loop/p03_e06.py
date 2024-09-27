'''
6	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數n，利用迴圈計算n!的值。
'''
import os
os.system("cls")

n = int(input("請輸入一個正整數："))
result = 1

for i in range(1, n+1):
    result *= i

print(f'{n}! = {result}')