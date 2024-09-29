import os
os.system("cls")
#數字判斷
# a = int(input('輸入成績：'))  
# if a> 90:print("so good!")    #內容只有一條敘述時，可和判斷式寫在同一行

'''
# 數字判斷
a = int(input('輸入成績：'))

if a >= 60 :
    print('成績',a, '及格')
print('判斷結束')
#文字判斷

a = input('是否列印結果：')
if a == '是' :
    print('成績及格')
print('判斷結束')
'''


a = int(input('輸入成績：'))
if a <=100 and a >=0:

    if a >= 60 :
        print('成績',a, '及格',end=" ")
        if a >= 90:
            print("表現優異")
  
print('判斷結束')


