'''
1	撰寫一個程式，由使用者輸入10個數字，然後找出最小值並且輸出
'''
import os
os.system('cls')

total = 10
max_num = 0
min_num = int(input('輸入數字：')) #min_num變數設在迴圈外
for i in range (total-1):
    num = int(input('輸入數字：')) #輸入其餘9個數
    if num < min_num:              #若num < min_num就交換
        min_num = num
    # print("目前最小的數字：",min_num)
    if num > max_num:
        max_num = num

print(f'最小的數字是{min_num}，最大的數字是{max_num}')
