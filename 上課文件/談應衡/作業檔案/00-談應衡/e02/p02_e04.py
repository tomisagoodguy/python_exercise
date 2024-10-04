'''
使用選擇敘述撰寫一個程式，讓使用者輸入兩個整數（每行一個）
及一個算術運算子（+  -  *  /  //  %）然後計算結果並且列印出來
'''
import os
os.system("cls")

a = int(input("輸入第1個整數："))
b = int(input("輸入第2個整數："))
opr = input("輸入算數運算子：")

if opr == "+" or opr == "-"or opr == "*" or opr == "/" or opr == "//" or opr == "%" :
    
    ans = 0               #初始值
    if opr == "+":  ans = a + b     #當內容敘述只有一行，可以直接寫在冒號之後
    elif opr == "-":  ans = a - b
    elif opr == "*":  ans = a * b
    elif opr == "/":  ans = a / b
    elif opr == "//":  ans = a // b
    elif opr == "%":  ans = a % b
    print ("%d %s %d = %d"%(a,opr,b,ans))

else:
    print("運算符號輸入錯誤")

