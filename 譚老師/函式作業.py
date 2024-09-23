import random
import os
os.system("cls")
'''
1.	建立一個函式compute()，讓使用者輸入學號、姓名、科系，透過呼叫顯示這些訊息。

'''
# def compute():
#     student_id =input("請輸入學號:")
#     name = input("請輸入姓名:")
#     department = input("請輸入科系:")

#     print("學生信息:")
#     print(f"學號:{student_id}")
#     print(f"姓名:{name}")
#     print(f"科系:{department}")

# compute()#呼叫函示

'''
2.	建立一個函式compute(x,y)。讓使用者輸入2個數字做為參數，透過呼叫函式，回傳(return x*y)的乘積。
'''
# def compute(x,y):
#     return x * y

# def main(): #主程序
#     num1 = float(input("請輸入第一個數字:"))
#     num2 = float(input("請輸入第二個數字:"))

#     result = compute(num1,num2)
#     print(f"{num1}*{num2}={result}")


# if __name__ == "__main__":
#     main()

'''
3.	讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳從x到y連續加總的結果。

'''

# def compute(x,y):
#     #確保 x是較小的數，y是比較大的數
#     if x > y:
#         x,y=y,x

#     total = sum(range(x,y+1))
#     return total

# def main():
#     x=int(input("請輸入第一個整數:"))
#     y = int(input("請輸入第二個整數:"))

#     result =compute(x,y)
#     print(f"從{x}到{y}的連續加總結果是:{result}")

# if __name__ == "__main__":
#     main()


'''
4.讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳x^y的值。
'''

# def compute(x,y):
#     return x**y

# def main():
#     x=int(input("請輸入底數 x:"))
#     y=int(input("請輸入指數 y:"))

#     result = compute(x,y)
#     print(f"{x}的{y}次方是:{result}")

# if __name__ == "__main__":
#     main()


'''
5.	建立一個函式compute(a,x,y) 使用者輸入3個參數：a (字元)、x(個數)、y(列數)，印出 y列 x個的a字元。
'''

# def compute(a,x,y):
#     for i in range(y): #重複y次(列數)
#         print(a*x) #打印x個a字符

# def main():
#     a= input("請輸入要打印的字符:")
#     x= int(input("請輸入每行的字符個數:"))
#     y= int(input("請輸入要打印的行數:"))

#     compute(a,x,y)


# if __name__ == "__main__":
#     main()
'''
6.	撰寫圓面積、長方形面積、三角形面積函式，透過輸入圓形半徑、長方形長、寬，三角形底和高，計算並輸出三個圖形面積與三個面積和。

'''

# import math

# def circle_area(r):
#     return math.pi*r**2

# def rectangle_area(length,width):
#     return  length * width

# def triangle_area(base,height):
#     return (base*height)/2

# def main():
#     r= float(input("請輸入圓形半徑"))
#     cir = circle_area(r)
#     print(f"圓形面積:{cir:.2f}")

#     length = float(input("請輸入長方形長度"))
#     width = float(input("請輸入長方形寬度"))
#     rec = rectangle_area(length, width)
#     print(f"長方形面積:{rec:.2f}")

#     base = float(input("請輸入三角形底"))
#     height = float(input("請輸入三角形高"))
#     tri = triangle_area(base, height)
#     print(f"三角形面積:{tri:.2f}")

#     total_area = cir+rec+tri
#     print(f"三個圖形面積和是:{total_area:2f}")

# main()

'''
7.	輸入2個正整數x,y，傳入最大公因數函式內，函式回傳最大公因數計算結果。
'''


# def gcd(x, y):

#     smaller = min(x, y)
#     # 從較小的數開始往下找，直到能同時整除x和y的數
#     for i in range(smaller, 0, -1):
#         if x % i == 0 and y % i == 0:
#             return i
# def main():
#     while True:
#         x= int(input("請輸入第一個正整數:"))
#         if x>0:
#             break
#         print("請輸入大於 0 的正整數。")
#     while True:
#         y = int(input("請輸入第二個正整數:"))
#         if y > 0:
#             break
#         print("請輸入大於 0 的正整數。")

#     result = gcd(x, y)
#     print(f"{x}和{y}的最大公因數是:{result}")

# main()


'''
8.	某市區停車場車位不足，為鼓勵車輛提早移出，進行如下規範：
(a). 2小時以內(含2小時)，每小時以30元計算
(b). 2小時以上到4小時(含4小時)，每小時以50元計算
(c). 4小時以上到6小時(含6小時)，每小時以80元計算
(d). 6小時以上，每小時以100元計算

請撰寫程式輸入停車時數，傳入函數參數內，函數傳回停車費計算結果。
'''
# def cal_fee(hours):
#     if hours<2:
#         return hours*30
#     elif hours<=4:
#         return 2*30+(hours-2)*50
#     elif hours <= 6:
#         return 2*30+2*50+(hours-4)*80
#     else:
#         return 2*30+2*50+2*80+(hours-6)*100
# def main():

#     hours = int(input("請輸入停車時數(小時):"))
#     if hours<0:
#         print("停車時數不能為負數:")
#     else:
#         fee = cal_fee(hours)
#         print(f"停車{hours}小時費用為:{fee}元")

# main()

'''
9.	使用函數撰寫骰子比大小程式，先由電腦模擬投擲三個骰子和，再由使用者輸入一個值(自訂)模擬投擲動作，透過亂數產生三個骰子和，並和電腦輸出結果比大小，印出"你贏了"或"你輸了"。

'''


def roll_dice():
    return sum(random.randint(1, 6) for i in range(3))


def compare_rolls(computer_roll, player_roll):
    print(f"電腦的點數:{computer_roll}")
    print(f"你的點數:{player_roll}")

    if player_roll > computer_roll:
        print("你贏了!")
    elif player_roll < computer_roll:
        print("你輸了!")
    else:
        print("平手!")


def main():
    computer_roll = roll_dice()

    while True:
        player_roll = int(input("請輸入你的點數(3到18之間):"))
        if 3 <= player_roll <= 18:
            break
        else:
            print("請輸入3到18之間的數字:")

    compare_rolls(computer_roll, player_roll)


main()
