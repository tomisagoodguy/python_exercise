'''
9	輸入3個正整數 a、b、c然後求出最大公因數
'''
import os
os.system('cls')

a = int(input('輸入正整數a：'))
b = int(input('輸入正整數b：'))
c = int(input('輸入正整數c：'))

gcd =1
k = 1

while k<=a or k<=b or k<=c:         # k大於a、b、c任何一個數的時候，迴圈結束
    if a % k == 0 and b % k == 0 and c % k == 0:  #a、b、c 可以同時被 k 整除，表示k是a、b、c公因素
        gcd = k                                   # 把公因數k寫入gcd(會覆蓋前一次寫入)，最後一次寫入的就是最大公因數
    k+=1
print (f'{a} {b} {c} 三個數的最大公因數是：{gcd}')