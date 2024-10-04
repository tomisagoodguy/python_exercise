'''
補充練習
驗證輸入內容，若錯誤可再輸入一次
共有三次輸入機會
'''
# '''
import os
os.system("cls")

pd = 'tvdiC201'
i = 1
while i <= 3 :
    a = input('請輸入驗證資料：')
    if a == pd :                #驗證內容是否正確
        print("通過!")
        i = 4
    elif i == 3 :               #驗證錯誤是否第三次
        print("不通過")
        i += 1
    else:                       #顯示還剩幾次機會
        print(f"不通過！你還有{3-i}次機會!")
        i += 1
print("判斷結束！")
# '''
#==================== 使用break ===================================
'''
pd = 'tvdiC201'
i = 0
while i < 3 :
    a = input('請輸入密碼：')
    i += 1
    if a == pd :
        print("通過!")
        break
    elif i == 3 :
        print("不通過")
    else:
        print(f"不通過！重新輸入!")
        
print("判斷結束！") 
'''  