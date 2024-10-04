'''
2.11.5	使用者輸入十個數字存放串列中，接著由大到小順序顯示最大的三個數字
'''
import os
os.system('cls')
lst = []

for i in range (0,10):
    lst.append(int(input(f'Input lst[{i}]= ')))
lst.sort(reverse=True)
# lst.sort()
print(lst)
for i in range(3):
# for i in range(-1,-4,-1):
    print('%d' %lst[i],end = ' ')