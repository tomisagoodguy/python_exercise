'''8.溫度轉換
請使用者輸入華氏溫度，然後輸出對應的攝氏溫度
溫度公式： 攝氏溫度 = (華氏溫度 - 32) *5/9
'''
F = float(input("請輸入華氏溫度："))
C = (F -32)*5/9
print("攝氏為：%.1f"%C)