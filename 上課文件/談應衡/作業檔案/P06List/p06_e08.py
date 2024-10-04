'''
2.11.8	設定一個串列，建立5個部門員工姓名，透過迴圈輸入員工成績，接下來依照成績排序輸出評核等級
成績	等級
90~100	A
80~89	B
70~79	C
60~69	D
60(不含)以下	E
'''

name = ['王大','老李','葉門','阿標','修仁',"小黃"]
score = [0]*len(name)
num = [90,80,70,60]
rank = ['A','B','C','D','E']


for i in range(len(name)):
    score[i] = eval(input(f'{name[i]}：'))
    if score[i] > 100:
        print('input error')
    # for j in range (len(rank)):
    #     if num[j] <= score[i]:
    #         score[i] = rank[j]

    if num[0] <= score[i]:
        score[i] = rank[0]
    elif num[1] <= score[i] <num[0]:
        score[i] = rank[1]
    elif num[2] <= score[i] <num[0]:
        score[i] = rank[2]
    elif num[3] <= score[i] <num[0]:
        score[i] = rank[3]
    else:
        score[i] =  rank[4]

for i in range(len(name)):
    print(f'{name[i]}成績為：{score[i]}')


