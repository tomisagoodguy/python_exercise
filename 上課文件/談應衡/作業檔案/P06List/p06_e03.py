'''
2.11.3	人工輸入12個正整數，存入串列，排序後輸出結果
'''
lst = []

for i in range (0,10):
    lst.append(int(input(f'Input lst[{i}]= ')))
lst.sort()
print(lst)
