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

#gpt寫法
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


# 5.使用選擇敘述撰寫一個程式，讓使用者輸入一個字元，判斷它是英文字母、數字、還是其他字元（如＄號）

# char = input("請輸入一個字元")

# if len(char)!=1:
#     print("請輸入一個字元")

a=123
len(a)