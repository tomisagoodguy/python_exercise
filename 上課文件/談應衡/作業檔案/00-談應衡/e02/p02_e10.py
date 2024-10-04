'''
使用選擇敘述撰寫一個程式，讓使用者輸入三個整數，由小到大排序後印出。
'''
import os
os.system("cls")

#方法一
'''
a,b,c = eval(input('輸入3個整數：'))
tmp = 0
if a > b:
    tmp = a
    a = b
    b = tmp

if b > c:
    tmp = b
    b = c
    c = tmp

if a > b:
    tmp = a
    a = b
    b = tmp
print('三個位數排序為：',a, b, c) 
'''
# 方法二
# '''
a,b,c = eval(input('輸入3個整數：'))

if a > b : a, b = b, a   #表示 a,b 和 b,a 內容進行交換

if b > c : b, c = c, b

if a > b : a, b = b, a

print('三個位數排序為：',a, b, c)

print("最大數：",max(a,b,c))

# '''