'''
9	使用者輸入一筆存款金額、年利率及經過的月份，並顯示每個月存款總額。輸出到小數點第二位數。
'''
import os
os.system("cls")

amount = eval(input('請輸入本金：'))
rate = eval(input('請輸入利率：'))
months = eval(input('請輸入月份：'))

total = amount
# print('%s \t %s' % ('Month','Amout'))
print("Month\t Amout")
for i in range (1, months + 1):
    total += total * rate /1200     #(/12月  利率100)
    # print('%3d \t %.2f'%(i,total))
    print(f"{i:3}\t{total:.2f}")
    

