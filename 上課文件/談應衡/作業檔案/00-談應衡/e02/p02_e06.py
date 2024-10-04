'''
使用選擇敘述撰寫一個程式，根據使用者輸入的分數顯示對應的等級。

 分數	   等級
90 – 100     A
80 - 90(不含) B
70 - 80(不含) C
60 - 70	(不含)D
60(不含)以下  F

'''
import os
os.system("cls")

score = float(input('請輸入成績：'))

if 90 <= score <=100:
    grade= 'A'

elif 80 <= score < 90:
    grade ='B'

elif 70 <= score < 80:
    grade= 'C'

elif 60 <= score < 70:
    grade= 'D'

else :
    grade= 'F'

print("成績為：",score,"等級：",grade)