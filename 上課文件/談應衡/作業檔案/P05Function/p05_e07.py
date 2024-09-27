# 7.	輸入2個正整數x,y，傳入最大公因數函式內，函式回傳最大公因數計算結果

def gcd(x,y):
    g = 0
    
#使用x,y兩變數中較小值(最大公因數不會超過兩數較小值)
    for i in range(1,min(x,y)+1): 
        if x % i == 0 and y % i == 0:
            g = i
    return g

def main():
    x = int(input('輸入x：'))
    y = int(input('輸入y：'))
    g = gcd(x,y)
    print(f'最大公因數：{g}')

main()