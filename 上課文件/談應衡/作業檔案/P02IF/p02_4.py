'''
範例：一元二次方程式　ax^2+bx+c　中，求解公式如下：b^2-4ac>0 有２個解，b^2-4ac＝0　有一個解，　b^2-4ac＜0　則無解。
'''

import os
os.system("cls")

a,b,c = eval(input("請輸入a, b, c三個數："))
d = b*b - 4 * a * c

if d > 0:
    print(d, "此方程式共有兩個解")

elif d == 0:
    print(d,"此方程式有一個解")

else:
    print(d,"此方程式無解")

print("判斷結束")

