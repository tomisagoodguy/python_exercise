import os
os.system("cls")
# """
num = eval(input("請輸入一個數字："))

if(num >= 85) and (num <= 95):
    print(f"{num} 在 85和95之間")
elif num <85:
    print (f"{num} 小於85" )
else:
    print(f"{num} 大於95" )
# """
#================ 巢狀 ========================
if num >= 85:
    if num <= 95:
        print("%d 在 85和95之間" % num)
    else:
        print("%d 大於95" % num)
else:
    print("%d 小於85" % num)

#=================================================

if 85 <= num <= 95:
    print("%d 在 85和95之間" % num)
elif num > 95:
    print("%d 大於95" % num)
else:
    print("%d 小於85" % num)