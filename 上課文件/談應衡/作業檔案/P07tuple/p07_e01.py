'''
1.	輸入數個整數並儲存至串列中，直到輸入-9999結束，再將此串列轉換成數(元)組，
最後顯示該數組以及長度、最大值、最小值、總和。
'''
num = []

while True:
    n = int(input('輸入整數(輸入 -9999 結束)：'))
    if n == -9999:
        break
    num.append(n)

n_tuple = tuple (num)
l_tuple = len(n_tuple)
max_tuple = max(n_tuple)
min_tuple = min(n_tuple)
Sum = sum(n_tuple)
print(n_tuple)
print('Length:',l_tuple,'\nMax:',max_tuple,'\nMin:',min_tuple)
print('Sum:',Sum)