import os
os.system('cls')
# 1	撰寫一個程式，由使用者輸入10個數字，然後找出最小值並且輸出
# numbers = []
# # 讓用戶輸入第一個數字，並假設它是最小的
# min_number = float(input("請輸入第一個數字:"))

# for i in range(2,11):
#     num = float(input(f"請輸入第{i}個數字"))
#     numbers.append(num)

# #假設第一個數字是最小的
# min_number = numbers[0]

# for number in numbers:
#     if number < min_number:
#         min_number = number

# print(f"您輸入的10個數字中，最小值是:{min_number}")

# 2	撰寫一個程式，由使用者輸入數字，輸入的動作直到輸入值為9999結束，然後找出其最小值並且輸出。

# numbers = []

# while True:
#     num = float(input("請輸入數字:"))

#     if num ==9999:
#         break
#     numbers.append(num)

# if len(numbers)>0:
#     min_number =numbers[0]

#     for number in numbers:
#         if number < min_number:
#             min_number = number

#     print(f"您輸入的數字中，最小值是:{min_number}")
# else:
#     print("你沒輸入任何數字")

'''
3	撰寫一個程式：
3.1	由使用者輸入兩個正整數a、b(a < b)
3.2	輸出從a到b(包含a 、b)之間4或9的倍數(一列輸出10個數字，欄寬為4、靠左對齊)。
3.3	輸出4或9的倍數共有幾個數。
3.4	輸出4或9的倍數加總和。
'''

# while True:
#     a = int(input("請輸入正整數a:"))
#     b = int(input("請輸入正整數b(b>a):"))
#     if a > 0 and b > a:
#         break
#     print("輸入無效，請確保a和b都是正整數，且b>a")

# # 初始化計數器和總和
# count = 0
# total = 0
# numbers = []

# # 尋找4或9的倍數:
# for num in range(a, b+1):
#     if num % 4 == 0 or num % 9 ==0:
#         numbers.append(num)
#         count +=1
#         total +=num

# #輸出結果
# print("\n4 或 9 的倍數")
# count = 0

# for num in numbers:
#     print(f"{num:<4}",end= " ")
#     count+=1
#     if count % 10 ==0:
#         print()#每10個數字換行

# if count % 10 !=0:
#     print()# 如果最後一行不滿10個數字，額外換行

# #計算輸出總數和總和
# total = 0
# for num in numbers:
#     total+=num

# print(f"\n4或9的倍數共有{len(numbers)}個數")
# print(f"4 或 9 的倍數的總和為 {total}")


'''
4	撰寫一個程式：
4.1	輸入一個正整數。
4.2	將這個正整數以反轉的順序輸出。
4.3	若輸入值為0，就輸出0
'''
# num = int(input("請輸入一個正整數"))

# if num==0:
#     print(num)
# else:
#     reversed_num = num%10 #初始化為個數
#     num=num//10 #去掉個位數
    
#     while num>0:
#         digit = num % 10
#         reversed_num = reversed_num*10 + digit
#         num = num//10

#     print(reversed_num)

'''
5	撰寫一個程式：
5.1	輸入代表成績的正整數。
5.2	根據分數與等級對照表，印出對應的等級。
5.3	輸入9999結束迴圈

'''

# while True:
#     score = int(input("請輸入成績(輸入9999結束)"))

#     if score == 9999:
#         print("程式結束")
#         break
#     if 90 <= score<=100:
#         grade="A"
#     elif 80 <= score<=89:
#         grade = "B"
#     elif 70 <= score <= 79:
#         grade = "C"
#     elif 60 <= score <= 69:
#         grade = "D"
#     elif 0 <= score <= 59:
#         grade = "E"
#     else:
#         grade = "無效的分數"

#     print(f'分數{score}的等級是:{grade}')


'''
以迴圈方式，提供使用者反覆輸入身高與體重，直到輸入9999結束。
計算出BMI值，並列印出相對應的意義。
輸出到小數點後第二位。
BMI公式： BMI = 體重(公斤) / 〖身高〗^2(〖公尺〗^2)

'''

# while True:
#     height = input("請輸入身高(公分)(輸入9999結束):")

#     if height =="9999":
#         print("程式結束")
#         break

#     weight = float(input("請輸入體重(公斤):"))
#     height = float(height)/100
#     bmi = weight/(height**2)

#     if bmi <18.5:
#         category = "過輕"
#     elif 18.5 <=bmi<=25:
#         category = "正常"
#     elif 25.0 <= bmi <= 29.9:
#         category = "過重"
#     else:
#         category = "肥胖"
    
#     print(f"您的BMI 值是:{bmi:2f}")
#     print(f"BMI類別 :{category}")
#     print()

'''
7	撰寫一個程式：
7.1	以迴圈方式，提供使用者反覆輸入西元年分，直到輸入9999結束。
7.2	判斷輸入年份是否為閏年。判斷規則為，每4年一閏，100年不閏，但400年也一閏
'''

# while True:
#     year = int(input("請輸入西元年分(輸入9999結束)"))

#     if year==9999:
#         print("程式結束")
#         break
    
#     if year % 400==0:
#         is_leap = True
#     elif year % 100 == 0:
#         is_leap = False
#     elif year % 4 == 0:
#         is_leap = True
#     else:
#         is_leap = False
    
#     if is_leap:
#         print(f"{year}年是閏年")
#     else:
#         print(f"{year}不是閏年")
    
#     print()


'''
8	撰寫一個程式：
8.1	輸入兩個西元年分，顯示兩個西元年分之間所有閏年。
8.2	每一列輸出10筆資料，並且對齊

'''


year1 = int(input("請輸入第一個西元年分"))
year2 = int(input("請輸入第二個西元年分"))

start_year = min(year1, year2)
end_year = max(year1, year2)

leap_year = []

for year in range(start_year, end_year+1):
    if year % 400 ==0 or (year % 4 ==0 and year % 100!=0):
        leap_year.append(year)

for i in range(0, len(leap_year),10):
    


