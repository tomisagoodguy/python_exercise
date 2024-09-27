'''8	撰寫一個程式：
8.1	輸入兩個西元年分，顯示兩個西元年分之間所有閏年。
8.2	每一列輸出10筆資料，並且對齊

'''
import os
os.system('cls')
c = 0
while True:
    try:
        y1,y2 = eval (input('輸入兩個西元年(逗號分隔)：'))
        break
    except:
        print("輸入錯誤！重新輸入")
        continue
for i in range(y1,y2+1):
    if i % 400 == 0 or (i % 4 == 0 and i % 100 != 0):
        print(f'{i:5d}',end='')
        c +=1
        if c % 10 == 0:
            print()