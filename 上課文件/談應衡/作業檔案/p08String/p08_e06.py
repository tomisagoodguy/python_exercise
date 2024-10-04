# 6.使用者輸入一個字串，字串為五個數字，以空白隔開，加總五個數字並計算平均
tol = 0
S = input("輸入五個數字，以空白隔開：")
lst = [int(i) for i in S.split(' ')] #使用迴圈，將字串分割出來的每個數字轉為整數
# print (lst)     #檢視串列內容

tol = sum(lst)
print ("數字總和為：",tol)