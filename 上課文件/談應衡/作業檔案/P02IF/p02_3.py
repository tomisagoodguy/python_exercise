import os
os.system("cls")
#數字判斷
'''
a = int(input('輸入1個數字：'))
if a > 0 :
    print(a, '大於0')
elif a < 0:
    print(a, '小於0')
else :
    print(a, '等於0')
print('判斷結束')
'''
#成績判斷
# '''
a = int(input('輸入成績：'))
if a >=0 and a <=100:
    if a >= 70 :
        print('表現正常')
    elif a >= 50:
        print('加強輔導')   
    else:
        print('建議重修')
else:
    print("輸入錯誤")
print('判斷結束')
# '''