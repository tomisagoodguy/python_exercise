import os
os.system("cls")

height = eval(input('請輸入身高(公分)：'))
weight = ((height/100) ** 2) * 21
print("建議適當體重為：%6.1f 公斤"%weight)

#下列程式做合理體重上下限
w1 = ((height/100) ** 2) * 18.5 #重量下限值
w2 = ((height/100) ** 2) * 24.9 #重量上限值

print("合適體重為：%6.1f 公斤到%6.1f之間"%(w1,w2))