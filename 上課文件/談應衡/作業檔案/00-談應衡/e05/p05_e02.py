'''
2.	建立一個函式compute(x,y)，讓使用者輸入2個數字做為參數，傳遞給一個名為compute(x,y)的函式，透過呼叫函式，回傳(return x,y)的乘積。
'''
import os
os.system('cls')

def compute(a,b):
    return a*b
#==========================
a = int(input("輸入第1個整數："))
b = int(input("輸入第2個整數："))
print (f'{a}*{b}={compute(a,b)}')