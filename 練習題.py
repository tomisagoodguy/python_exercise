# x=123
# y=123456
# z=12
# p=12
# q=123
# r=123456
# print(f"{x:>8},{y:>8},{z:>8}")
# print(f"{p:>8},{q:>8},{r:>8}")

#單位換算
# a = float(input("請輸入公斤:"))*2.20462
# print(a,"磅")

#平均值計算
#畫面顯示"請輸入第x筆資料："三次，由鍵盤輸入3個整數，並分別存入3個變數。計算這3個整數的平均值，平均值取到小數第二位並輸出。
#input("請輸入第X筆資料")

# x= 1
# a= float(input(f"請輸入第{x}筆資料"))
# x +=1
# b= float(input(f"請輸入第{x}筆資料"))
# x +=1
# c= float(input(f"請輸入第{x}筆資料"))
# mean =int((a + b+ c)/3)
# print(f"平均值:{mean}")


#4.	兩點距離計算：
# import math
# x1= float(input("請輸入第1組x座標"))
# y1= float(input("請輸入第1組y座標"))

# x2 =float(input("請輸入第2組x座標"))
# y2= float(input("請輸入第2組y座標"))

# d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print(f"兩點({x1},{y1})和({x2}和{y2})之間的距離是:{d:2f}")

'''
5.	存錢筒：
	於畫面顯示[請輸入您的姓名:]，執行時輸入姓名。
	於畫面顯示要求輸入銅板個數，並依序要求輸入1元、5元、10元、50元硬幣數量。
	輸出總金額。
'''

# name = str(input("請輸入您的姓名"))
# coin_1 = int(input("輸入1元硬幣數量"))
# coin_5 = int(input("輸入5元硬幣數量"))
# coin_10 = int(input("輸入10元硬幣數量"))
# coin_50 = int(input("輸入50元硬幣數量"))
# average = coin_1*1 + coin_5*5 + coin_10*10 + coin_50*50
# print(f"總金額是:{average}")


'''
#6. 使用math 計算數學函數 f(x) = 3x^3+2x-1，x值透過input()輸入
import math

def f(x):
    return 3*math.pow(x,3)+2*x-1

x = float(input('請輸入x值'))
result = x

print(f"f({x})={result}")
'''

'''
7.	圖形面積

圓的半徑=5，PI=3.1415926，圓面積計算公式:半徑平方*PI，請計算圓面積。
三角形的底=10，高=5，三角形面積公式:底*高/2，請計算三角形面積。
長方形的長=5，寬=10，長方形面積公式:長*寬，請計算長方形面積。
圖形面積=圓面積+三角形面積+長方形面積。

'''

# import math
# r=5
# 圓面積面積 = math.pi * r**2

# 底=10
# 高=5
# 三角形面積 = ((底*高)/2)

# 長方形的長=5
# 長方形的寬=10
# 長方形面積=(長方形的長*長方形的寬)

# 圖形面積=(圓面積面積+三角形面積+長方形面積)
# print(f"圖形面積:{圖形面積:2f}")

'''
8.	溫度轉換
寫一個程式，請使用者輸入華氏溫度，然後輸出對應的攝氏溫度
溫度公式： 攝氏溫度 = (華氏溫度 - 32) *5/9
'''
# tem = float((input("請輸入華氏溫度")))
# 攝氏溫度 = float((tem - 32) *5/9)
# print(f"攝氏溫度:{攝氏溫度:2f}")

tall = float( input("請輸入身高(m)"))
weight = float( input("請輸入體重(kg)"))
BMI = weight/tall**2
print(f"BMI:{BMI:2f}")

