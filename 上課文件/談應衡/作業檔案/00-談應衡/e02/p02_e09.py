'''
使用選擇敘述撰寫一個程式，讓使用者可以輸入三邊長，檢查這三邊長是否能組成一個三角形，
若可以則輸出三角形周長，否則顯示 "不能成為三角形"  (三角形任兩邊長總和大於第三邊)
'''
import os
os.system("cls")

side1 = eval(input('輸入三角形第1邊：'))
side2 = eval(input('輸入三角形第2邊：'))
side3 = eval(input('輸入三角形第3邊：'))

if side1 + side2 > side3 \
    and side2 + side3 > side1 \
    and side3 + side1 > side2:      #反斜線表示同一敘述換行
    print("周長",side1+side2+side3)
else:
    print("不是三角形")