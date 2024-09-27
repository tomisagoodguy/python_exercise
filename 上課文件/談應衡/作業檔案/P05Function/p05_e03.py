'''
3.使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳從x到y連續加總的結果。
'''
def compute(a,b):
    return int((a+b)*(b-a+1)/2)

n1 = eval(input("輸入第1個整數："))
n2 = eval(input("輸入第2個整數："))

print(compute(n1,n2))