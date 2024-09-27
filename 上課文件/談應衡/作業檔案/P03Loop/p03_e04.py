'''
4	使用迴圈敘述撰寫程式，讓使用者輸入一個正整數a，利用迴圈計算從1到a之間(含)所有5的倍數和。
'''
import os
os.system("cls")

a = int(input("請輸入一個正整數："))
ans = 0
#======== 方法一 ===========
for i in range(1, a+1):
    # print("i=",i)
    if i % 5 == 0:
        ans += i

print(ans)
#======== 方法二 ===========
ans = 0

for i in range(5,a+1,5):
    # print ("i=",i)
    ans += i

print(ans)