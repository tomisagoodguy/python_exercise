'''
2	撰寫一個程式，由使用者輸入數字，輸入的動作直到輸入值為9999結束，然後找出其最小值並且輸出
'''
import os
os.system('cls')
min_num = int(input('輸入數字：')) #min_num變數設在迴圈外
num = min_num

while num != 9999:
    num = int(input('輸入數字：'))
    if num < min_num:
        min_num = num

print(f'最小的數字是{min_num}')