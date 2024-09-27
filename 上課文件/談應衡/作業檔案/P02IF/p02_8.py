import os
os.system("cls")
#檢查是否為英文字元
ch = input('輸入英文字母：')
if ch >= 'A' and ch<= 'Z' or ch >='a' and ch <= 'z':  #先and 後 or
    print('ok')
else:
    print('非英文字母')

#檢查是否為大寫英文字母
ch = input('輸入大寫英文字母：')
if ch >= 'A' :
    if ch<= 'Z':
        print('ok')
    else:
        print('非大寫英文字母')
else:
    print('非大寫英文字母')