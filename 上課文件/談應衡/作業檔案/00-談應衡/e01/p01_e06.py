'''6. 數學函數
使用mathc函數 計算數學函數 f(x)=3(x^3)+2x-1 ，x值透過input()輸入
'''
# import math
x = eval(input("請輸入x的值："))
# y = 3*(math.pow(x,3))+2*x-1     # x 的3次方以math.pow表示
# y = 3*(pow(x,3))+2*x-1 
y = 3*(x**3)+2*x-1
 
print(f"f({x})={y}")