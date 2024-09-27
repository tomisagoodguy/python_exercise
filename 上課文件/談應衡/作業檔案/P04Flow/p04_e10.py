'''
10	完美數：一個數如果恰好等於它的因數(不含數字本身)之和，這個數就稱為[完美數]。
請使用 for 迴圈設計一程式，輸入一個值，找出這個值以內的所有完美數，執行結果如範例。
執行結果
請輸入一個數： 1000
1 ~ 1000 完美數有: 6  28  496  
'''
import os
os.system('cls')

a = int(input('請輸入一個正整數：'))

print('完美數有：')
for i in range(1,a+1):
    n = 0
    for j in range (1,i):
        if i % j ==0:
            n += j
    if n == i:
        print(f'{n:4}',end = ' ')


'''
a = int(input('請輸入一個正整數：'))

print('完美數有：')
for i in range(1,a+1):
    n = 0
    for j in range (1,i//2 + 1):
        if i % j ==0:
            n += j
    if n == i:
        print(f'{n:4}',end='')
'''