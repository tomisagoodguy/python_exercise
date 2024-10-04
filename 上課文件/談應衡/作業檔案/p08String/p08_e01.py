# 1.使用者輸入一個字串，顯示該字串的每一個字元索引

S = input("輸入一個字串：")
for i in range(len(S)):
    print('第%d個字元為 %s' % (i,S[i]))