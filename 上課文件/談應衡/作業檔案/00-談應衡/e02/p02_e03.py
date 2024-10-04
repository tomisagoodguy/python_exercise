'''
使用選擇敘述撰寫一個程式，讓使用者輸入一個西元年分，判斷是否為閏年。
閏年規則為每四年一次，但滿百年不閏，可是每四百年還是會閏一次。
'''
import os
os.system("cls")

year = int (input("請輸入西元年："))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("西元%d年是閏年" %year)

else:
    print("西元%d年不是閏年" %year)