'''
5.	建立一個函式compute(a,x,y) 使用者輸入3個參數：a (字元)、x(個數)、y(列數)，印出 y列 x個的a字元。
'''

def compute(a,x,y):
    for i in range(y):
        for j in range(x):
            print(a,end ='')
        print()

a = input("輸入一個字元：")
x = int(input("輸入個數："))
y = int(input("輸入列數："))

compute(a,x,y)