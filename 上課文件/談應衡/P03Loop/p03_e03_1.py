'''
3	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數 (<30)然後以三角形方式依序輸出此數階乘結果
'''
# '''
import os
os.system("cls")

try:
    num = int(input("請輸入一個小於30的正整數："))

    if num > 30 :
        print("輸入錯誤!")

    else:
        for i in range (1 , num+1):
            
            for j in range(1, i+1):
                # print("%d"%(i*j),end =" ")
                print(f'{i*j}',end =" ")
                
            print()
# except :
except ValueError :
    print("輸入型別錯誤!")
# '''
