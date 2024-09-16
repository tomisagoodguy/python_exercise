'''4. 2點間距離
請使用math.pow 及 math.sqrt 撰寫程式，顯示如[請輸入第1組的x座標:]的方式， 分別顯示第一組與第二組x,y座標輸入畫面。
輸入第二組座標(x2,y2)，並輸出兩組座標之間的距離。
'''
import math  #載入數學函數
x1,y1 = eval(input("請輸入x1,y1座標(以逗號分隔)")) # eval()可以同時輸入兩個數，但中間要用逗號分隔
x2,y2 = eval(input("請輸入x2,y2座標(以逗號分隔)")) 
x = math.pow((x2-x1),2)    #次方函數，"2"表示2次方
# x = (x2-x1)**2
y = math.pow((y2-y1),2)
# y = (y2-y1)**2
line = math.sqrt(x+y)      #開根號
# line = (x+y)**(1/2)
print (line)

# line = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))
# print (line)