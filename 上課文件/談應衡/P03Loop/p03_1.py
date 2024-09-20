import os
os.system("cls")

# while loop

'''
i = 0       #初始值
while i < 10:  #表示i 小於 10時迴圈會執行   條件判斷
    print(i,end=' ')
    i += 1    #控制條件
print("程式結束")
'''

# 1+2+3+...+100
'''
total = 0
i = 1          #設定迴圈運算初始值
while i < 101: #迴圈條件運算式
    total += i  #迴圈主體敘述(total = total + i)
    i += 1      #迴圈控制式 (在迴圈主體敘述內) i=i+1
print ('total =',total)
'''

# for...in range loop
'''
for i in range (0,11,1): 
    print(i,end=" ")

for x in range(11): #使用初始值 star=0,step=1可免
  print(x,end=" ")
print()
for x in range(1, 11):
  print(x,end=" ")
print()
for x in range(1, 11, 2):
  print(x,end=" ")
'''

# 1+2+3+...+100
'''
total = 0
for i in range(1,101,1):  #迴圈初始值為1 結束值為101-1 每次加1(可省略)
    total += i            #迴圈主體敘述
print ('total =',total )
'''

# 巢狀迴圈(nested loop)
'''
print('=====')
for x in range(1,6):        #第一層迴圈
    print(f"x = {x}")
    for y in range(1,6):    #第二層迴圈
        print (f'    y ={y}')
    print('=====')
print("程式結束")
'''
'''
print('=====')
x=1
while x < 6:
    print('x = %d'%x) 
    y=1
    while y < 6:
        print ('    y = %d'%y)
        y +=1
    print('=====')
    x+=1
print("程式結束")
'''
#99 multiple table version 1
'''
for x in range(1,10):
    for y in range(1,10):
        print(f'{x}*{y} = {x*y:2}')
    print()
'''
#99 multiple table version 2
'''
for x in range(1,10):
    for y in range(1,10):
        print(f'{x}*{y} = {x*y:<2}',end = ' ')
    print()
'''
#99 multiple table version 3
'''
for x in range(1,10):
    for y in range(2,10):
        # print ('%d*%d= %2d'%(y,x,x*y),end = ' ')
        print(f'{y}*{x}={x*y:2}',end='  ')
    print()
'''

# for i in range(10,0,-1):
#     print(i)
'''
num = int(input("請輸入一個小於30的正整數："))

if num > 30 :
    print("輸入錯誤!")

else:
    for i in range (1 , num+1):
        
        for j in range(1, i+1):
            # print("%d"%(i*j),end =" ")
            print(f'{i*j}',end =" ")
            
        print()
'''
