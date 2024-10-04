# '''
import os
os.system('cls')

import random
a = random.choice('123')        #從"123"字串中隨機選出一個字元
win = 0
lose = 0
while True:
    b = input ('輸入1.剪刀  2.石頭 3.布：')

    #個人出拳
    #若if 後方僅單一敘述，可精簡列於同一行
    if b == "1" : m="出剪刀"  
    elif b=="2" : m="出石頭"
    elif b=="3" : m="出布"
    else : m="亂輸入"

    #電腦出拳
    if a == '1': c ="剪刀"
    elif a == '2': c ="石頭"
    else : c="布"

    print(f"電腦出{c}，你{m}")

    #比輸贏
    if a == b : print("平手")   #將敘述與條件式放在同一行

    elif (a == '1' and b =='2' )or  (a == '2' and b=='3')or (a == '3' and  b=='1'): 
        print ("你贏了！")
        win += 1

    elif (b == '1' and a =='2' )or  (b == '2' and a=='3')or (b =='3' and  a=='1'): 
        print ("你輸了！")
        lose += 1

    else: print("輸入錯誤")

    if win >=2 and lose <2 or win == 3 :
        print("獲勝")
        break
    elif lose >=2 and win < 2 or lose == 3:
        print("失敗")
        break
    else:
        print("繼續")

print('遊戲結束！')
# '''