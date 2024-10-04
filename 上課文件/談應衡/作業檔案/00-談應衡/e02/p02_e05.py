'''
使用選擇敘述撰寫一個程式，讓使用者輸入一個字元，
判斷它是英文字母、數字、還是其他字元（如＄號）
'''
import os
os.system("cls")
c = input('輸入一個字元：')

if('a' <= c <= 'z') or ('A'<= c <= 'Z'):
    print(c,"：英文字母")

elif('0' <= c <= '9') :
    print(c,"：數字")

else:
    print(c,"：其他字元")