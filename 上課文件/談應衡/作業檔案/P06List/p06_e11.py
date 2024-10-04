'''
1.	輸入兩個正整數，當作串列的 列數 與 行數 ，每個位置存放內容為那個位置本身的 "行數索引值" 減去 "列數索引值" 的結果。
'''
def compute(lst):
    for i in range(len(lst)):
        for j in range(len(lst[i])):
            print("%4d"%lst[i][j],end='')
        print()
#============以下為主程式======================
row = int(input("輸入列數："))
column = int(input("輸入行數："))
lst = []

for i in range(row):
    lst.append([])
    for j in range(column):
        lst[i].append(j - i)

compute(lst)        #列印結果


