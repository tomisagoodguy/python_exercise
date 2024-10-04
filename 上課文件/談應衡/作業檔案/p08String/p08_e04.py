# 4.使用者輸入一個字串，將字串1.全部改為大寫。2.每個字第一個字母改為大寫。
# 輸入範例： Practice makes perfect.
S = input("輸入一個字串：")
S1 = S.upper()   #全部改大寫
S2 = S.title()   #每個字第一個字母改大寫
print(f"1.{S1} \n2.{S2}")