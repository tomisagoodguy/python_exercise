'''
初始值
while 條件式:
        主體敘述
        (控制式)

i=0
while i<=10:
        x=x+i
        i=i+1
        print(x,end="")

        

i=i+1 equal i+=1
'''
import os
os.system("cls")


# # 步驟 1: 設定兩個正整數 (模擬使用者輸入)
# a = 1  # 模擬使用者輸入的第一個正整數
# b = 100  # 模擬使用者輸入的第二個正整數

# print(f"第一個正整數 a: {a}")
# print(f"第二個正整數 b: {b}")

# # 步驟 2: 檢查輸入是否符合條件 (a < b 且都是正整數)
# if a <= 0 or b <= 0:
#     print("錯誤：請輸入正整數")
# elif a >= b:
#     print("錯誤：a 必須小於 b")
# else:
#     # 步驟 3: 初始化總和變數
#     總和 = 0

#     # 步驟 4: 使用迴圈計算總和
#     for 數字 in range(a, b+1):
#         總和 += 數字

#     # 步驟 5: 輸出結果
#     print(f"從 {a} 加到 {b} 的總和是：{總和}")

# print("程式執行完畢。")

# for x in range(10):
#     print(x, end=" ")


# 計算 1 到 100 的總和
total = 0
for i in range(1, 101):
    total += i

print("1 到 100 的總和是:", total)

