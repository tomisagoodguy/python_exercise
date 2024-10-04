'''
2.11.7	使用迴圈反覆輸入成績直到-9999結束，輸出最大值、最小值，加總與平均
'''

lst = []

while True:
    a = eval(input('輸入成績：'))
    if a == -9999:
        break
    else:
        lst.append(a)

tol = sum(lst)
print('最大值：',max(lst),'最小值：',min(lst))
print('總分：%.2f，平均：%.2f'%(tol,tol/len(lst)))