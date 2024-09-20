'''
1	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的總和。
'''
import os
os.system("cls")

a = int(input('請輸入第一個正整數：'))
b = int(input('請輸入第二個正整數：'))
# a,b = 0,0
# while a<=0 and b<=0:
#     a,b = eval(input('請輸入兩個正整數，以逗號區隔，計算兩數間所有整數和：'))

if a > b:       #檢查初始值小於結束值
    a,b = b,a   #若a > b 兩數互換

total = 0

for i in range(a,b+1,1):
    total += i
    
print("total =",total)