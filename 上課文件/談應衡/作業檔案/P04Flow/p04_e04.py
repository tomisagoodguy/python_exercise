'''
4	撰寫一個程式：
4.1	輸入一個正整數。
4.2	將這個正整數以反轉的順序輸出。
4.3	若輸入值為0，就輸出0
'''
import os
os.system('cls')

n = int(input("輸入正整數："))

if n != 0:
    while n != 0:
        a = n % 10
        n //= 10
        print(a,end ='')

else:
    print(n)

   
   