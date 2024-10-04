'''
2.	輸入三位學生各五筆平時測驗成績，接著計算並輸出每位總分與平均
'''
score = []
num = ['1','2','3']

for i in range (len(num)):
    print ('輸入%s 號學員平時成績：'% num[i])
    score.append([])
    for j in range (1,6):
        score[i].append(eval(input(f'第{j}次成績：')))

for i in range (len(num)):
    tol = sum(score[i])
    avg = tol / len(score[i])
    print("第%s學生：" % num[i])
    print("總分：%d" % tol)
    print("平均：%.2f" % avg)