'''
2.11.2	上述樂透程式，加上串列檢查，當檢查出元素有重複時，替換該元素
'''
#新增一個檢查串列chknum，1~49位置存放0 一旦存放資料就改為1
import random
lotto = []      #串列存放樂透碼
chknum = []     #串列存放確認碼

for i in range(1,50): #串列1~49存放0
    chknum.append(0)

count = 1
while count <= 6:    
    num = random.randint(1,49) #樂透號碼1~49
    if chknum [num] == 0:      #對照數字位置若為0就存入資料，並把狀態改為1
        lotto.append(num)
        count += 1
    chknum[num] = 1

print("本期樂透號碼")
for i in lotto:         #串列迴圈i為迴圈內的值
    print ("%4d"%i,end='')
#===========================================================
