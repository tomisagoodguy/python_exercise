import os
os.system("cls")

a = int(input('輸入1個數字：'))
if a > 0 :print(a, '大於0') 
else:print(a, '小於等於0')
    

    
print('判斷結束')

# a = int(input('輸入成績：'))
# if a >= 60 :
#     print('成績',a, '及格')
#     if a>=90:
#         print("表現優異！")
#     else:
#         print("還有進步空間")
# else:
#     print(a, '不及格，再加油！')
# print('判斷結束')

a = input("請輸入蘋果的英文：")
if a == "apple" or "Apple":
    print("符合")
else:
    print("不符合")
print("判斷結束")
