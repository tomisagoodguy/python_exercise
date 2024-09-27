'''
4.讓使用者輸入2個整數，呼叫函式compute(x,y) 並傳送2個參數給函數，讓函數回傳x^y的值。
'''
def compute(a,b):
    return a**b

n1 = int(input("輸入第1個整數："))
n2 = int(input("輸入第2個整數："))

print(compute(n1,n2))