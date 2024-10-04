'''
6.	撰寫圓面積、長方形面積、三角形面積函式，透過輸入圓形半徑、長方形長、寬，三角形底和高，計算並書出三個圖形面積與三個面積和
	rectangle 、circle、triangle
'''
import os
os.system('cls')

def rectangle(x,y):     #長方形
    area = x*y
    return area

def circle(r):         #圓形
    area = r*r*3.14159
    return area

def triangle(x,y):      #三角形
    area = x*y/2
    return area

def main():
    
    x,y = eval(input('請輸入矩形長與寬(逗號分隔)：'))
    a1 = rectangle(x,y)
    x,y = eval(input('請輸入三角形底與高(逗號分隔)：'))
    a2 = triangle(x,y)
    r = eval(input('請輸入圓形半徑(逗號分隔)：'))
    a3 = circle(r)

    print('面積總和為：',a1+a2+a3)

main()
