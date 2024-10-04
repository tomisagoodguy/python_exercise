'''
9.  使用函式撰寫骰子比大小程式，先由電腦模擬投擲三個骰子和，再由使用者輸入一個值(自訂)模擬投擲動作，透過亂數產生三個骰子和，並和電腦輸出結果比大小，印出"你贏了"或"你輸了"。
'''
import os
os.system('cls')
'''
import random
def running():

    r = 0
    for i in range(0,3):
        r = r + (random.randint(1,6))

    l = 0
    for i in range(0,3):
        l = l + (random.randint(1,6))

    print(f"電腦點數：{r}，你的點數{l}")
    compare(r,l)

def compare(r,l):

    if r > l : 
        print("你輸了")
    elif r == l:
        print("平手")
    else:
        print("你贏了")


a = input('投擲骰子：(Y)')
if a != 'Y' and a!= 'y':
    print ("遊戲結束")
else:
    running()
'''
#=======================================================
import random
def running():

    r = 0
    for i in range(0,3):
        r = r + (random.randint(1,6))
    return r

def compare(r,l):

    if r > l : 
        print("你輸了")
    elif r == l:
        print("平手")
    else:
        print("你贏了")


a = input('投擲骰子：(Y)')
if a != 'Y' and a!= 'y':
    print ("遊戲結束")
else:
    m = running()
    c = running()
    compare(m,c)
