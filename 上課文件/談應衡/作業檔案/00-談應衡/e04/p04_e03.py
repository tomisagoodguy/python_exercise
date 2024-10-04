'''
3	撰寫一個程式：
3.1	由使用者輸入兩個正整數a、b (a<b)
3.2	輸出從a到b(包含a 、b)之間4或9的倍數(一列輸出10個數字，欄寬為4、靠左對齊)。
3.3	輸出4或9的倍數共有幾個數。
3.4	輸出4或9的倍數加總和。

'''
import os
os.system('cls')

count = 0
total = 0
a,b = eval(input('請輸入兩個正整數 a, b (逗號分隔)：'))
if a > b:       #確認a < b
    a,b = b,a

for i in range (a,b+1):
    if i % 4 == 0 or i % 9 ==0:
        print(f'{i:4}',end = '') 
        total += i                  #符合4或9倍數的數字加總
        count += 1                  #計算符合4或9的倍數一共幾個
        if count % 10 == 0:         #每輸出10個數字跳行
            print()

print('\n4或9的倍數一共有%d個，總和為%d'%(count,total))