import random
import os
os.system("cls")


'''
1	使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的總和。例如：輸入a=1、b=100 (1+2+3+…+100)，則輸出結果為5050
'''

# a=int(input("請輸入第一個正整數 a: "))
# b=int(input("請輸入第二個正整數 b (b必須大於a): "))

# if a < b :
#     total = 0
#     for i in range(a,b+1):
#         total +=i
#     print(f"從{a}加到{b}的總和是{total}")
# else:
#     print("錯誤:a必須小於b。")

'''

2	
使用迴圈敘述撰寫程式，讓使用者輸入兩個正整數 a、b (a<b) ，利用迴圈計算從a開始連加到b的偶數總和。例如：輸入a=1、b=100 (2+4+6+…+100)，則輸出結果為2550

'''

# a=int(input("請輸入第一個正整數 a: "))
# b=int(input("請輸入第二個正整數 b (b必須大於a): "))

# if a < b :
#     if a % 2 !=0:
#         start = a+1
#     else:
#         start = a

#     total = 0
#     for i in range(start,b+1,2):
#         if i % 2 ==0:
#             total +=i

#     print(f"從{a}加到{b}的偶數總和是{total}")
# else:
#     print("錯誤:a必須小於b。")


'''
3	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數 (<30)然後以三角形方式依序輸出此數階乘結果

'''

# n = int(input("請輸入一個正整數(小於30):"))

# if 0 < n < 30:
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             result = i*j
#             print(f"{result:3d}",end=" ")

#         print()#換行

'''
4	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間(含)所有5的倍數和。
'''

# a = int(input("請輸入正整數"))

# sum = 0
# for i in range(5,a+1,5):
#     sum += i
# print(f"從1到{a}之間所有5的倍數和是:{sum}")

'''
5	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，將此數反轉順序輸出 (利用 % 與 // 處理)
'''
# num = int(input("請輸入一個正整數"))
# #初始化反轉後的數字
# reversed_sum = 0

# while num >0 :
#     #獲取最後一位數
#     digit = num%10
#     reversed_sum = reversed_sum*10 +digit

#     num = num//10
# print("反轉後的數字是:", reversed_sum)


# # 獲取用戶輸入的正整數
# num = int(input("請輸入一個正整數："))

# # 將數字轉換為字符串
# num_str = str(num)

# # 初始化反轉後的數字
# reversed_num = 0

# # 使用 for 迴圈從右到左遍歷數字的每一位
# for digit in num_str[::-1]:
#     # 將當前數字轉換回整數並加到反轉後的數字中
#     reversed_num = reversed_num * 10 + int(digit)

# # 輸出反轉後的數字
# print("反轉後的數字是：", reversed_num)

'''
6	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數n，利用迴圈計算n!的值。
'''
# n = int(input("請輸入正整數"))

# if n<0:
#     print("錯誤，請輸入非負整數")
# elif n==0:
#     print("0! = 1")
# else:
#     f = 1
#     for i in range(1,n+1):
#         f*= i
#     print(f"{n}!={f}")


'''
7	(1) 請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數n (n < 10)，顯示 n*n乘法表。
(2)每項運算式格式化排列整齊，每個運算子與運算元輸出的欄寬為2，而每項乘積輸出的欄寬為4，皆靠左對齊不跳行。
# 獲取用戶輸入
n = int(input("請輸入一個正整數 n (n < 10): "))

# 檢查輸入是否有效
if n <= 0 or n >= 10:
    print("輸入無效，請輸入1到9之間的整數。")
else:
    # 外層迴圈控制行數
    for i in range(1, n + 1):
        # 內層迴圈控制列數
        for j in range(1, n + 1):
            # 計算乘積
            product = i * j
            # 格式化輸出
            print(f"{i:<2}*{j:<2}={product:<4}", end="")
        # 每行結束後換行
        print()

'''

'''
8	請使用迴圈敘述撰寫程式，讓使用者輸入一個正整數，代表後面要測試的次數。 每次測試都是輸入一個正整數，將所有位數加起來輸出結果
8.1	輸入說明： 請輸入一個正整數，代表要測試數字的”次數”。
   每次輸入一個兩位數以上資料。
8.2	輸出說明： 看所有位數加總和
8.3	若輸入大於或等於10，顯示”輸入錯誤！數字不能大於或等於10”

輸出結果：
請輸入測試次數 2
請輸入正整數 32145
  32145 數字拆開後相加為 15
請輸入正整數 654789
  654789 數字拆開後相加為 39
'''

'''
test = int(input("請輸入測試次數"))
if test >= 10:
    print("輸入錯誤！數字不能大於或等於10")
else:
    for i in range(test):
        num = int(input("請輸入正整數"))
        # 檢查輸入是否為兩位數以上
        if num < 10:

        
'''


'''
9	使用者輸入一筆存款金額、年利率及經過的月份，並顯示每個月存款總額。輸出到小數點第二位數。
例：存款10000 年利率5.75%
滿一個月，存款為：10000+10000*5.75/1200=10047.92
滿二個月，存款為：10047.92+10047.92*5.75/1200=10096.06
滿三個月，存款為：10096.06+10096.06*5.75/1200=10144.44 餘下類推
輸出結果：
請輸入本金50000
請輸入利率3
請輸入月份5
Month    Amout
  1      50125.00
  2      50250.31
  3      50375.94
  4      50501.88
  5      50628.13

'''

# principal = float(input("請輸入本金:"))
# annual_rate = float(input("請輸入年利率:"))
# months = int(input("請輸入月份:"))

# monthly_rate = annual_rate/12/100

# current_amount = principal
# print("Month    Amount")

# for month in range(1,months+1):
#     current_amount*=(1+monthly_rate)
#     print(f"{month:4d}  {current_amount:2f}")
# 獲取用戶輸入

