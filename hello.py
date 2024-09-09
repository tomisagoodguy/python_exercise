# print("hello world")
# print("hello world")
# print('6+8',14)

# print(format(變數名稱,"格式化參數"))

'''
x=4
y=5
print(x,"+",y ,'=',x+y)
print(f"{x} + {y}= {x+y}") # f是format的意思，格式f"{}"  
print(f"{x:2} + {y:4}= {x+y}")#{x:2}代表空2格，對齊可以用

a=123
b=456.789
c="python"
print(format(a,"5d")) #d表示整數，5d表示顯示5位數
print(format(b,"10.2f"))#float，共顯示10位數(含小數點後2位)
print(format(c,"10s"))#string,這裡顯示10個字
print(format(a,"<5d"))#"<"表示往左對齊
print(format(b,"<10.2f"))
print(format(c,">10s"))#">"往右對齊
'''

'''
格式化輸出
print("格式化參數"%(變化名稱))
'''
a=123
b=456.789
c="python"

print("%5d"% (a)) #d表示整數，5d表示至少顯示5位數
print("%10.2f"% (b))#float，共顯示10位數(含小數點後2位)
print("%10s"%(c))#string,這裡顯示10個字
print("%-5d"%(a))#-向左對齊
print("%-10.2f"%(a))#-向左對齊
print("%-10s"%(c))#-向左對齊

a = input("請輸入你的名字")
print("您好"+a)

