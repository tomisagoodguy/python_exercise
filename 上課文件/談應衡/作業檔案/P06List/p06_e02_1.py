'''
2.11.2	上述樂透程式，加上串列檢查，當檢查出元素有重複時，替換該元素
(使用not in)
'''
import os
os.system('cls')
import random
lotto = []          #串列存放樂透碼
#------------------------------------------------------
#使用for迴圈，定數迴圈，當出現重複時，會少出一個樂透碼
# for i in range (1,7): #6個樂透數
#     num = random.randint(1,49) #樂透號碼1~49
#     if num not in lotto:
#         lotto.append(num)
#         print ("%4d"%num,end='')
    
#------------------------------------------------------
'''
print("本期樂透號碼")
x = 0
while x < 6:
    num = random.randint(1,49) #樂透號碼1~49
    if num not in lotto:
        lotto.append(num)
        x += 1
        print ("%4d"%num,end='')
'''
#-------------------------------------------------------
# '''
import random
number = [x for x in range(1,50)] #產生1 ~ 49 串列內容
# print (number)
lotto = random.sample(number, k=6) #產生6個隨機碼
print("本期樂透號碼\n",lotto)
# '''