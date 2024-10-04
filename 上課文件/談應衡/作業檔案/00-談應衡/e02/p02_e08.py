#溫度轉換
'''
請使用者輸入攝氏或華氏溫度，然後輸出對應的攝氏溫度
溫度公式：F表示攝氏，C表示華氏
F = 9/5 * C + 32 
C = (F - 32) * 5/9
'''
import os
os.system("cls")

A = input("輸入(1)華氏 或(2)攝氏 溫度：")
if A == '1':
    F = eval(input("請輸入華氏溫度："))
    C = (F - 32)*5/9
    print("攝氏為：%.1f"%C)
    if C < 10:
        print('現在溫度%.1f，注意保暖'% C)
    if C >28:
        print("現在溫度%.1f，當心中暑" % C)

elif A == '2':
    C = eval(input("請輸入攝氏溫度："))
    F = 32 + C * 9/5
    print("華氏為：%.1f"%F)
    if C < 10:
        print('現在溫度%.1f，注意保暖'% F)
    if C > 28:
        print("現在溫度%.1f，當心中暑" % F)    

else:
    print("輸入錯誤!")

