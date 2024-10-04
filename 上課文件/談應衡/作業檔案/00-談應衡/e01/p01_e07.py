'''7.面積計算
圓的半徑=5，PI=3.1415926，圓面積計算公式:半徑平方*PI，請計算圓面積。
三角形的底=10，高=5，三角形面積公式:底*高/2，請計算三角形面積。
長方形的長=5，寬=10，長方形面積公式:長*寬，請計算長方形面積。
圖形面積=圓面積+三角形面積+長方形面積。

'''
import math
# circle = math.pow(5,2)*math.pi
# circle = pow(5,2)*3.1415926     
circle = 5*5*3.14159        #圓面積
triangle = 10*5/2           #三角形面積
rectangle = 5*10            #長方形面積
# print("面積和為：%.4f"%(circle+triangle+rectangle))
print(f"面積和為：{circle+triangle+rectangle:.2f}")
