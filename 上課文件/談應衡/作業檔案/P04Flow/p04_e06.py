'''	
撰寫一個程式：
	以迴圈方式，提供使用者反覆輸入身高與體重，直到輸入9999結束。
	計算出BMI值，並列印出相對應的意義。
	輸出到小數點後第二位。
BMI公式： BMI = 體重(公斤) / 〖身高〗^2(〖公尺〗^2)
BMI	        說明
< 18.5	    過輕
18.5 - 24.9	正常
25.0 - 29.9	過重
> 30	    肥胖

'''
import os
os.system('cls')
state = ""
height = eval(input("輸入身高："))
while height != 9999:
    weight = eval(input("輸入體重："))
    bmi = weight/((height/100) **2)
    if weight == 9999:
        break
    elif bmi >= 30:
        state = "過胖"
    elif 25 <= bmi < 30:
        state = "超重"
    elif 18.5 <= bmi < 25:
        state = "正常"
    elif bmi < 18.5:
        state = "太輕"
    print("BMI：%.2f" % bmi)
    print("體質: %s："%state)
    
    height = eval(input("輸入身高："))
