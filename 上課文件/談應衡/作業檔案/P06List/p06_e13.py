'''
3.	建立一個3 * 3的串列矩陣，內容為鍵盤輸入的整數(不能重複)，接著輸出矩陣最大與最小值的索引
'''
# def max_min():
#     a = c = mat [0][0]      #設定變數 a、c等於串列mat[0][0]的內容(比大小初始值)
#     b = d = 0               #設定c、d為0 (索引值用)
 
#     for i in range (0,m):   #使用迴圈，逐一檢查"每一列"中的最大值
#         if a < max(mat[i]): #使用max函數查詢 mat第[i]列的最大值和a的內容比較
#             a = max(mat[i]) #若a < mat[i]列中，最大值，就改寫a的內容
#             b = i           #把b 設為目前最大值 所在列的編號
     
#         if c > min(mat[i]):
#             c = min(mat[i])
#             d = i

#     # e = mat[b].index(a)
#     print(f"mat[{b}][{mat[b].index(a)}] 最大值：{a}")  #用index索引mat[b]列中，a的位置  
#     print(f"mat[{d}][{mat[d].index(c)}] 最小值：{c}") 

def max_min():
    ma = []
    mi = []
    for i in range(m):
        ma.append(max(mat[i]))
        mi.append(min(mat[i]))

    print(f'最大值：{max(ma)} ,最小值：{min(mi)}')

#====================以下為主程式==============================
mat = []
m = 3

for i in range(0,m):
    mat.append([])
    for j in range(0,m):
        mat[i].append(int(input(f"輸入整數[{i}][{j}]:")))
# print(mat)
max_min()
