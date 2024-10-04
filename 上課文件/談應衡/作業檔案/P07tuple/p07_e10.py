'''
10.	輸入五筆資料放在 tuple10 的數組，之後印出數組每一個元素，以及找出此數組最大值、最小值、總和。
'''
tup10 = ()
for i in range(5):
    a = int(input(f"輸入整數，{i+1}/5："))
    
    tup10 += (a,)

print(tup10)
print("最大值：",max(tup10))
print("最小值：",min(tup10))
print("總和：",sum(tup10))