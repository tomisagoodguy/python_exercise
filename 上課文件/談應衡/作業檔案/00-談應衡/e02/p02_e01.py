'''
使用選擇敘述撰寫一個程式，讓使用者輸入一個正整數，判斷是奇數還是偶數
'''
import os
os.system("cls")

a = int(input("請輸入正整數："))

if a % 2 == 0 :
    print("%d是偶數" %a)

else:
    print("%d這是奇數" %a)
#=================================
#輸入檢查
# try:
#     a = int(input("請輸入正整數："))
#     print(a)
# except ValueError:
#     print("輸入錯誤")