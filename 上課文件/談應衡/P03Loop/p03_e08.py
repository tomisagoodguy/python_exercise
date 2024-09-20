'''
8	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，代表後面要測試的次數。
    每次測試都是輸入一個正整數，將所有位數加起來輸出結果
'''
import os
os.system("cls")

total = int(input('請輸入測試次數 '))

for i in range(total):
    num = int(input('請輸入正整數 '))
    tmp = num
    sum_digit = 0
    while tmp != 0:
        sum_digit += tmp % 10
        tmp //= 10

    # print(" sum of all digits of %d is %d" %(num,sum_digit))
    # print("  %d 數字拆開後相加為 %d" %(num,sum_digit))
    print(f"{num} 數字拆開後相加為 {sum_digit}")