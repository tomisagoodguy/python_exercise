'''
4.	輸入數個整數儲存到集合，直到-9999結束，顯示這個集合的長度、最大值、最小值、總和。
'''
set1 = set()

while True:
    n = int(input("Enter an integer:"))
    if n == -9999:
        break
    else:
        set1.add(n)

print(set1)
print("Length:",len(set1),"\nMax:",max(set1),"\nMin:",min(set1))
print("Sum:",sum(set1))
