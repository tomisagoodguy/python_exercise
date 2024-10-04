'''
2.11.1	使用隨機方式產生樂透號碼 6組，並存放入串列中，印出結果。
'''
# '''
import random
lotto = []          #串列存放樂透碼
for i in range (1,7): #6個樂透數
    num = random.randint(1,49) #樂透號碼1~49
    lotto.append(num)
print(lotto)
print("本期樂透號碼")
for i in lotto:         #串列迴圈i為迴圈內的值
    print ("%4d"%i,end='')
# '''
#==============================================================
'''
import random
number = [x for x in range(1,50)]
lotto = random.choices(number, k=6) #產生6個隨機碼
print("本期樂透號碼\n",lotto)
'''