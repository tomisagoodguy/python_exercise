#7.使用者輸入一串序號，格式為ddd-dd-ddd ，d為數字。檢查輸入格式正確，則輸出"格式正確！"，否則輸出"格式錯誤！"

S = input("請輸入序號：")
sn = len(S) == 10               #若資料長度為10 sn 設為True，不等設為False
if sn:                          # if sn == True 簡化寫法
    for i in range(len(S)):
        if i == 3 or i == 6:    #位址3和6的字元必須是 '-' 號
            if S[i] != '-':
                sn = False      #不是'-'號將sn 設為False
                break
        elif not S[i].isdigit(): #位址3和6以外的字元必須是數字
            sn = False           #若不是，sn設為False
            break
if sn:
    print("格式正確！")
else:
    print("格式錯誤！")

 




