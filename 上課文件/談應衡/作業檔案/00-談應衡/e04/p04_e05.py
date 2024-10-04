'''
5	撰寫一個程式：
5.1	輸入代表成績的正整數。
5.2	根據分數與等級對照表，印出對應的等級。
5.3	輸入9999結束迴圈
分數	    等級
90 ~ 100	A
80 ~ 89	    B
70 ~ 79	    C
60 ~ 69	    D
0 ~ 59	    E
'''
import os
os.system('cls')

score = 0

while True:
    score = int(input('輸入成績：'))
    if score == 9999:
        break
    
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    elif 0 <= score <= 59:
        grade = 'E'
    else:
        grade ="輸入錯誤!"

    print(grade)