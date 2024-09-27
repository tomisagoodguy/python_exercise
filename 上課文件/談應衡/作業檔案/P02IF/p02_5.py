'''
BMI計算
'''
import os
os.system("cls")

height = eval(input('請輸入身高(公分)：'))
weight = eval(input('請輸入體重(公斤)：'))

BMI = weight / (height/100) ** 2    #BMI公式計算(身高轉換為公尺)
print(f"你的BMI值為：{BMI}")
# '''
if BMI < 18.5 :
    w1 = ((height/100) ** 2) * 18.5
    w = w1 - weight
    print(f"體重過輕，要再增重{w:.1f}公斤")

elif BMI < 25.0 :
    print("體重正常")

elif BMI < 30 :
    w2 = ((height/100) ** 2) * 24.9
    w = weight - w2
    print(f"體重過重,至少再減重{w:.1f}公斤")

else:
    w2 = ((height/100) ** 2) * 24.9
    w = weight - w2
    print(f"體重太胖了,至少再減重{w:.1f}公斤")
# '''
