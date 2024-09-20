import random as ra
import os
os.system('cls')


# random.seed()  #初始化隨機數，若()內設定數字，無論隨機幾次都會產生固定結果
# r=random.random()  #隨機產生0-1(不含1)的浮點數
# print(r)
#r = random.uniform(1, 50)  # 隨機產生1-50的浮點數
#r = random.randint(1, 10) #隨機產生1-50的浮點數
# r = random.randrange(1, 50, 2)  # 隨機產生1-49的整數(奇數)
#r = random.choice([5, 8, 7, 4, 66, 33, 99, 45])  # 從串列中隨機產生1個數字
# r = random.choices([5, 8, 7, 4, 66, 33, 99, 45], k=4)  # 從串列中隨機產生指定個數數字(會重複)

#r = random.sample([5, 8, 7, 4, 66, 33, 99, 45], k=4)  # 從串列中隨機產生指定個數數字(不重複)
# print(r)  


# 使用亂數產生器產生10個亂數。
# for i in range(1,11):
#     randnum = ra.randint(1,100)
#     print(f"{randnum}",end = " ")


#若要檢查產生的亂數中有多少個是偶數或是奇數，此時就必須藉助選擇敘述來判斷。

# even = 0
# odd = 0
# for i in range(1,11):
#     randnum  = ra.randint(1,100)
#     print(randnum,end = " ")
#     if randnum %2 ==0:
#         #如果 randnum 是偶數，even 計數器加 1；否則，odd 計數器加 1。
#         even +=1
#     else:
#         odd +=1
# print('\n even= %d,odd=%d'%(even,odd))

