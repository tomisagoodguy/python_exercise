'''
9.BMI計算
'''

height = float(input('請輸入身高(公分)：'))
weight = float(input('請輸入體重(公斤)：'))

BMI = weight / (height/100) ** 2    #BMI公式計算(身高轉換為公尺)
# print("你的BMI值為%6.2f"%BMI)
print(f"你的BMI值為{BMI:6.2f}")
#建議體重：
weight = ((height/100) ** 2) * 22
print("建議適當體重為：%6.1f 公斤"%weight)
