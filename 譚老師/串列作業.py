import random
from collections import Counter
import os
os.system('cls')

'''
1.使用隨機方式產生樂透號碼 6個數字(1~49)，並存放入串列中，印出結果。
'''


# lottery_numbers = random.choices(range(1,50),k=6)
# print("樂透號碼是(允許重複)是:", lottery_numbers)

# # 從 1 到 49 中隨機選擇 6 個不重複的數字
# numbers = random.sample(range(1, 50), 6)
# print(numbers)

'''
2.11.2	上述樂透程式，加上串列檢查，當檢查出元素有重複時，替換該元素
'''

# def uni_lottery():
#     numbers=[]
#     while len(numbers)<6:
#         num = random.randint(1,49)
#         if num not in numbers:
#             numbers.append(num)
#     return numbers

# lottery = uni_lottery()
# print("隨機生成不重複樂透號碼是:", lottery)

'''
2.11.3	人工輸入12個正整數，存入串列，排序後輸出結果
'''
# numbers = []

# for i in range(12):
#     while True:
#         num = int(input(f"輸入第{i+1}個數字:"))
#         if num > 0 :
#             numbers.append(num)
#             break
#         else:
#             print('請輸入正整數!')

# numbers.sort()
# print("排序後的數字是：", numbers)

'''
2.11.4	隨機輸出五張撲克牌，不論花色，點數存放到串列中，計算點數。
'''
# def card():
#     card_values = {
#         '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
#         '10': 10, 'J': 11, 'Q': 10, 'K': 10, 'A': 1  }

#     card_list = list(card_values)

#     drawn_cards = random.sample(card_list,5)

#     total_points = sum(card_values[card]for card in drawn_cards)

#     return drawn_cards,total_points


# cards, points = card()

# print("抽取的撲克牌是：", cards)
# print("總點數是：", points)


'''
2.11.5	使用者輸入十個數字存放串列中，接著由大到小順序顯示最大的三個數字。
'''
# numbers= []
# print("請輸入時個數字")
# for i in range(10):
#     num = float(input(f"請輸入第{i+1}個數字"))
#     numbers.append(num)

# numbers.sort(reverse=True)
# top_three = numbers[:3]
# print('最大的三個數字是:',top_three)
'''
2.11.6	使用者輸入十個數字，做為樣本數，輸出眾數(出現最多次數的數字
'''
# numbers= []
# print("請輸入十個數字:")

# for i in range(10):
#     num = float(input(f"請輸入第 {i+1} 個數字: "))
#     numbers.append(num)

# count = Counter(numbers)
# mode = count.most_common(1)[0][0]
# print("眾數是：", mode)  

'''
2.11.7	使用迴圈反覆輸入成績，存放到串列，直到-9999結束，輸出最大值、最小值，加總與平均
'''

# grades= []

# print("請輸入成績,輸入-9999結束:")

# while True:
#     grade = float(input("請輸入成績:"))
#     if grade ==-9999:
#         break
#     grades.append(grade)

# if grades:
#     max_grade = max(grades)
#     min_grade = min(grades)
#     sum_grades = sum(grades)
#     average_grade = sum_grades / len(grades)

#     # 輸出結果
#     print(f"最大值: {max_grade}")
#     print(f"最小值: {min_grade}")
#     print(f"加總: {sum_grades}")
#     print(f"平均: {average_grade:.2f}")
# else:
#     print("未輸入任何有效成績。")

'''
2.11.8	設定一個串列，建立5個部門員工姓名，透過迴圈輸入員工成績，接下來依照成績排序輸出評核等級

'''

# 設定一個串列，包含5個部門員工姓名
# employees = ['張三', '李四', "王五", '趙六', '前七']

# # 創建一個空列表來存儲員工成績
# scores = []

# # 使用迴圈為每個員工輸入成績
# for employee in employees:
#     while True:
#         # 提示用戶輸入當前員工的成績
#         score = float(input(f"請輸入{employee}成績(0-100)"))
#         # 檢查輸入的成績是否在有效範圍內
#         if 0 <= score <= 100:
#             # 如果成績有效，將其添加到scores列表中
#             scores.append(score)
#             # 跳出while循環，進入下一個員工的成績輸入
#             break
#         else:
#             # 如果成績無效，提示用戶重新輸入
#             print('成績必須在0到100之間，請重新輸入:')

# # 定義一個函數來根據成績評定等級


# def get_grade(score):
#     if 90 < score <= 100:
#         return "A"
#     elif 80 < score <= 90:
#         return "B"
#     elif 70 < score <= 80:
#         return "C"
#     elif 60 < score <= 70:
#         return "D"
#     else:
#         return "E"


# # 創建一個空列表來儲存員工的所有信息(姓名、成績、等級)
# employee_data = []

# # 使用range()函數來遍歷員工和成績列表
# for i in range(len(employees)):
#     name = employees[i]
#     score = scores[i]
#     grade = get_grade(score)
#     # 將每個員工的數據（姓名、成績、等級）添加到列表中
#     employee_data.append((name, score, grade))

# # 對員工數據進行排序，根據成績從高到低排序
# employee_data.sort(key=lambda x: x[1], reverse=True)

# # 輸出排序後的員工數據
# for data in employee_data:
#     name, score, grade = data
#     print(f"{name}\t{score:.1f}\t{grade}")
