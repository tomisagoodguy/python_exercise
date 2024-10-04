'''
使用選擇敘述撰寫一個程式，要求使用者輸入一個8000以上的金額後，輸出顯示輸入金額和折扣優惠以後的金額。
   金額	        折扣
8,000(含)以上	9.5折
18,000(含)以上	9折
28,000(含)以上	8折
38,000(含)以上	7折

'''
import os
os.system("cls")

cost = eval(input('結帳金額：'))

if cost >= 38000:
    pay = cost * 0.7
elif cost >= 28000:
    pay = cost * 0.8
elif cost >= 18000:
    pay = cost * 0.9
elif cost >= 8000:
    pay = cost * 0.95
else:
    pay = cost

print("折扣後金額：",pay)
