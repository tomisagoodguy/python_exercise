import os
os.system("cls")

# a = int(input("輸入成績"))

# # 要縮排，不然執行的時候>=60會直接跳最後一行
# if a >= 60:
#     print("成績", a, "及格")
# print("判斷結束")


a = int(input("輸入成績"))
if a <= 100 and a >= 0:

    if a >= 60:
        # end=""可以把兩行連起來
        print("成績", a, "及格", end=" ")
        if a >= 90:
            print("good")
print("判斷結束")
