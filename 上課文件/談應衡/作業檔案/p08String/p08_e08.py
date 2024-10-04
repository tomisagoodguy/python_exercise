'''
8.使用者輸入一組字串，檢查是否符合規則：
1.至少8個字元，2.有英文字母和數字，3.至少有一個大寫英文字母。
符合顯示"密碼已設定"，不合顯示"密碼設定不符規則"
'''

pwd = input("請輸入密碼：")
chk = len(pwd) >= 8                                 #至少8個字元
if chk:
    if pwd.isalpha() or pwd.isdigit() or pwd.islower(): #不能全部英文、數字、小寫字母
        chk = False
    else:                                               #檢查是否只有英文字母和數字(不能是特殊符號)
        for i in range(len(pwd)):                       #把輸入內容用迴圈逐一檢查，不能有英文與數字以外符號
            if not pwd[i].isalpha() and not pwd[i].isdigit():
                chk = False                             
                break

if chk :
    print("密碼已設定")
else:
    print("密碼設定不符規則")