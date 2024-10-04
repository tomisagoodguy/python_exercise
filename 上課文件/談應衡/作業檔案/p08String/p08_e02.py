
# 2.使用者輸入一個字串，顯示每個字元對應的ASCII碼，並將ASCII碼加總

total = 0
S = input("輸入一個字串：")

for i in range(len(S)):
    num = ord(S[i])     # ASCII 轉換
    print(f"{S[i]}的ASCII碼為{num}")
    total += num
print(f"ASCII的總和為{total}")