'''
猜大小，猜數字比7大或比7小
1.輸入押注金
2.輸入玩法：1.猜大小 2.猜點數 0.離開
猜大小贏2倍
猜數字贏10倍
反覆玩至按0離開
'''
import random
    
while True:
    n = random.randint(1,13)
    b = int(input("押注："))
    a = input("1.猜大小 2.猜點數 0.離開：")
  
    if a == '0':
        print('離開')
        break
    elif a == '1':
        c = input("比7大按0,比7小按1：")
        print(f"電腦數字為：{n}")
        if (n > 7 and c=='0') or (n < 7 and c=='1') :
            print(f"你贏了！獎金{b*2}元")
        else:
            print(f"再接再厲!")
    elif a == '2':
        c = int(input("輸入點數(1-13)："))
        if (n == c):
            print(f"你贏了！獎金{b*10}元")
        else:
            print(f"再接再厲!")
    else:
        print("輸入錯誤，請重來")
