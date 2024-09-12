import os
os.system('cls')
# 1.	使用選擇敘述撰寫一個程式，讓使用者輸入一個正整數，判斷是奇數還是偶數

# num = int(input("請輸入正整數"))
# if num >=0 and (num/2)!=0 :
#     print("奇數")
# else:
#     print("偶數")


# 2.	使用選擇敘述撰寫一個程式，讓使用者輸入一個正整數，判斷是否為3或5的倍數，然後輸出＂這個數是3和5的倍數＂或＂這個數是3的倍數＂或＂這個數是5的倍數＂、＂這個數不是3或5的倍數＂，輸出時可以將字串中＂這個數＂改為輸入的變數值

# num = int(input("請輸入一個正整數："))

# if num > 0:
#     if num % 3 == 0 and num % 5 == 0:
#         print(f"{num}是3和5的倍數")
#     elif num % 3 == 0:
#         print(f"{num}是3的倍數")
#     elif num % 5 == 0:
#         print(f"{num}是5的倍數")
#     else:
#         print(f"{num}不是3或5的倍數")
# else:
#     print("請輸入一個正整數")


# 3.	使用選擇敘述撰寫一個程式，讓使用者輸入一個西元年分，判斷是否為閏年。閏年規則為每四年一次，但滿百年不閏，可是每四百年還是會閏一次。

# num = int(input("輸入一個西元年分"))
# if num >= 0:
#     if num % 100 == 0 and num % 400 == 0:
#         print(f"{num}是閏年")
#     elif num % 100 == 0:
#         print(f"{num}不是閏年")
#     elif num%4==0:
#         print(f"{num}是閏年")
#     else:
#         print(f"{num}不是閏年")

# 4.	使用選擇敘述撰寫一個程式，讓使用者輸入兩個整數（每行一個）及一個算術運算子（ + - * / // % ） ，將計算結果並且將整個算式列印出來

# num1 = int(input("輸入第一個整數"))
# num2 = int(input("輸入第二個整數"))
# operator = (input("輸入算術運算子（ + - * / // % ）:"))

# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
# elif operator == "/":
#     result = num1 / num2
#     if num2 == 0:
#         print("錯誤:除數不能為零")
# elif operator == "//":
#     if num2 == 0:
#         print("錯誤:除數不能為零")
#     result = num1 // num2
# elif operator == '%':
#     if num2 == 0:
#         print("錯誤：除數不能為零")
#     result = num1 % num2
# else:
#     print("錯誤：無效的運算符")

# print(f"{num1} {operator} {num2} = {result}")

# gpt寫法
'''
num1 = int(input("輸入第一個整數："))
num2 = int(input("輸入第二個整數："))
operator = input("輸入算術運算子（ + - * / // % ）：")

result = None  # 初始化 result 變量

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator in ["/", "//", "%"]:
    if num2 == 0:
        print("錯誤：除數不能為零")
    else:
        if operator == "/":
            result = num1 / num2
        elif operator == "//":
            result = num1 // num2
        else:  # operator == '%'
            result = num1 % num2
else:
    print("錯誤：無效的運算符")

if result is not None:
    print(f"{num1} {operator} {num2} = {result}")

'''


"""
len() 函數的用途：
len() 函數用於返回對象的長度。它主要用於序列類型的對象，如字符串、列表、元組等。
"""

# 5.使用選擇敘述撰寫一個程式，讓使用者輸入一個字元，判斷它是英文字母、數字、還是其他字元（如＄號）

# char = input("請輸入一個字元")

# if len(char) != 1:
#     print("請輸入一個字元")
# elif (char >= "A" and char <= "Z") or (char >= "a" and char <= "z"):
#     print(f"{char}是一個英文字母")
# elif (char>="0" and char<="9"):
#     print(f"{char}是一個數字")
# else:
#     print(f"{char}是其他字元")


# score = int(input("請輸入分數"))
# if score <= 0 or score > 100:
#     print("請輸入0到100之間的分數")
# elif score>=90 :
#     print("A")
# elif score >=80 :
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")


# 7.	使用選擇敘述撰寫一個程式，要求使用者輸入一個8000以上的金額後，輸出顯示輸入金額和折扣優惠以後的金額。

# try:
#     money = int(input("請輸入8000以上的金額："))

#     if money >= 38000:
#         discounted_money = money * 0.7
#     elif money >= 28000:
#         discounted_money = money * 0.8
#     elif money >= 18000:
#         discounted_money = money * 0.9
#     elif money >= 8000:
#         discounted_money = money * 0.95
#     else:
#         print("輸入的金額必須是8000以上")
#         exit()

#     print(f"原本的金額是{money}；折扣後是{discounted_money:.0f}")

# except ValueError:
#     print("請輸入有效的數字")

"""
try:
    # 可能引發異常的代碼
except ValueError:
    # 處理 ValueError
except TypeError:
    # 處理 TypeError
except:
    # 處理所有其他異常

"""

"""
8.	請使用者輸入攝氏或華氏溫度，然後輸出對應的華氏或攝氏溫度。
溫度公式：C表示攝氏，F表示華氏
F = 9/5 * C + 32 
C = (F - 32) * 5/9。

upper() 是 Python 中字串（string）對象的一個方法。它的主要功能是將字串中的所有字母轉換為大寫。
lower() 方法的作用是將字串中的所有字母轉換為小寫
"""

# temp_type = input("請輸入溫度類型（C 代表攝氏，F 代表華氏）：").upper()
# temp = float(input("請輸入溫度"))

# if temp_type == "C":
#     result = (9/5 * temp) + 32
#     print(f"{temp:.1f}°C 等於 {result:.1f}°F")
# elif temp_type == "F":
#     result = (temp - 32) * 5/9
#     print(f"{temp:.1f}°F 等於 {result:.1f}°C")
# else:
#     print("請輸入 C 或 F")


"""
9.	使用選擇敘述撰寫一個程式，讓使用者可以輸入三邊長，檢查這三邊長是否能組成一個三角形，
若可以則輸出三角形周長，否則顯示 "不能成為三角形"  (三角形任兩邊長總和大於第三邊)
"""

# side1 = float(input("請輸入第一邊長"))
# side2 = float(input("請輸入第二邊長"))
# side3 = float(input("請輸入第三邊長"))

# if (side1+side2 > side3) and (side2 + side3 > side1) and (side1+side3 > side2):
#     perimeter = side1 + side2 + side3
#     print(f"這些邊長可以組成三角形")
#     print(f"三角形的周長是:{perimeter:2f}")
# else :
#     print("不能組成三角形")

"""
10.	使用選擇敘述撰寫一個程式，讓使用者輸入三個整數，由小到大排序後印出。
"""

# num1 = int(input("請輸入第一個整數"))
# num2 = int(input("請輸入第二個整數"))
# num3 = int(input("請輸入第三個整數"))

# if num1 > num2:
#     num1, num2 = num2, num1
# if num2 > num3:
#    num2, num3 = num3, num2
# if num1 > num3:
#    num1, num3 = num3, num1

# print(f"由小到大排序後的結果是：{num1}, {num2}, {num3}")


num1 = int(input("請輸入第一個整數"))
num2 = int(input("請輸入第二個整數"))
num3 = int(input("請輸入第三個整數"))

numbers = [num1, num2, num3]
numbers.sort()

print(f"由小到大的排序結果是:{numbers[0]},{numbers[1]},{numbers[2]}")
