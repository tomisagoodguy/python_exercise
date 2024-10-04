'''
5.	使用者建立四週各三天溫度，接著計算並輸出這四周的平均溫度，及最高最低溫。
'''

Week = 4
Day = 3
temp = []

for i in range(Week):
    temp.append([])
    print('第 %d 週：'%(i+1))
    for j in range(Day):
        temp[i].append(eval(input('第 %d 日：'%(j+1))))

comb = []
for i in range(Week):
    comb.extend(temp[i]) #將temp[i]內容加入comb中，成為一維串列

avg = sum(comb) / (Week * Day)
print('Average:%.2f'%avg)
print('Highest:',max(comb))
print('Lowest:',min(comb))