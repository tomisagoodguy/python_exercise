import os
os.system('cls')

'''
1.	輸入兩個正整數，當作串列的 列數 與 行數 ，每個位置存放內容為那個位置本身的 "行數索引值" 減去 "列數索引值" 的結果。
'''

# def create_matrix(rows,cols):
#     matrix=[]

#     for row_index in range(rows):
#         row = []
#         for col_index in range(cols):
#             value = row_index - col_index
#             row.append(value)
#         matrix.append(row)
#     return  matrix

# rows = int(input("請輸入行數:"))
# cols = int(input("請輸入列數:"))

# matrix = create_matrix(rows, cols)
# for row in matrix:
#     print(row)

'''
2.	輸入三位學生各五筆平時測驗成績，接著計算並輸出每位總分與平均
'''

# def calculaie_total_and_average(scores):
#     total = sum(scores)
#     average = total / len(scores)
#     return total,average

# students_scores = []

# for i  in range(3):#輸入3位學生的成績
#     print(f"請輸入第{i+1}位學生的五比測驗成績:")
#     scores = []
#     for j in range(5):
#         score= float(input(f"成績{j+1}:"))
#         scores.append(score)

#     students_scores.append(scores)

# for i, scores in enumerate(students_scores):
#     total, average = calculaie_total_and_average(scores)
#     print(f"學生 {i+1} 的總分是: {total}，平均是: {average:.2f}")


'''
3.	建立一個3 * 3的串列矩陣，內容為鍵盤輸入的整數(不能重複)，接著輸出矩陣最大與最小值的索引。
'''

matrix= []

#這是一個集合，用來記錄你輸入過的數字，卻保不重複
input_set = set()