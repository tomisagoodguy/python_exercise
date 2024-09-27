#密碼輸入只允許錯三次
import os
os.system('cls')

x = 3   #密碼次數
y = 0   #輸入次數
b = 3399

for i in range(x):
    a = int(input ("請輸入資料："))
    y += 1

    if a == b:
        print ("通過")
        break
    elif y < 3:
        print(f"不通過，還有{x-y}次機會")
    else:
        print ("不通過")