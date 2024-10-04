'''
輸入售票訂單，每筆訂單可選擇票種和人(張)數，結算金額後可選擇是否進行下一筆訂單
'''
import os
os.system("cls")

next ="y"
while next == "y":
    
    # tol = 0
    ticket = 0
    p1,p2,p3 =0,0,0
    pay = 0
    tk = "a"
    while tk == 'a':

        ticket =int(input("1.生日優惠票,2.全票,3.優惠票,9.離開計算："))
        if ticket == 9:
            tk = 'q'
        else:    
            audi = int(input("輸入人數："))

        if ticket == 1:
            price = 220
            na = "生日優惠票："
            p1 = 220*audi
            print(f"{na}{audi}張，{p1}元")
        elif ticket == 2:
            price = 320
            na = "全票："
            p2 = 320*audi
            print(f"{na}{audi}張，{p2}元")
        elif ticket == 3:
            price = 270
            na = "優惠票："
            p3 = 270*audi
            print(f"{na}{audi}張，{p3}元")
        else:
            print('離開!')

    pay = p1+p2+p3
    print(f"結算金額：{pay}")

    next = input("下一位(按y表示繼續，否則退出)：")