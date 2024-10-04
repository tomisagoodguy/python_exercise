'''
2	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，
利用迴圈計算從a開始連加到b的偶數總和。
例如：輸入a=1、b=100 (2+4+6+…+100)，則輸出結果為2550
'''
import os
os.system("cls")

a = int(input('請輸入第一個正整數：'))
b = int(input('請輸入第二個正整數：'))

if a > b:       #若a > b 兩數互換
    a,b = b,a

total = 0
for i in range(a, b+1):
    if i % 2 ==0:
        total+=i

print("total =",total)
#===============================================
'''
a = int(input('請輸入第一個正整數：'))
b = int(input('請輸入第二個正整數：'))
# a,b = eval(input('請輸入兩個正整數：'))

if a > b:       #若a > b 兩數互換
    a,b = b,a
    
total = 0
if a % 2 != 0:
    a = a+1
for i in range(a,b+1,2):
    total += i
    
print("total =",total)
'''