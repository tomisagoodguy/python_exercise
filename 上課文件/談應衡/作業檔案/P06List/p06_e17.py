'''
7.  主程式 main()中，讓使用者輸入不重複的10個數字到串列，
將串列傳遞給 compuet()函式，函式接收一個串列lst 和一個變數 a (預設值為3)，
並傳回lst中a個最大數字，將結果回傳主程式 main()輸出。
'''

def compute(lst, a):
    lst.sort(reverse = True)
    ans = []

    for i in range(a):
        ans.append(lst[i])
    return ans

def main():
    lst =[]
    i = 1
    while i <=10:
        num = eval(input(f'輸入第{i}個整數：'))
        if num not in lst:
            lst.append(num)
            i+=1

    a = input('傳回幾個最大數字：')
    if a == "":
        a = '3'

    print(lst)
    print(compute(lst,eval(a)))

main()
