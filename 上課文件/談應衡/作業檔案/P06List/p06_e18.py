'''
8.	使用lotto ()產生6組樂透號碼，並以main()函式呼叫5次lotto()函式產生五組號碼，並由小到大排序出來。
'''
import random
def lotto():
    lottoLst = []
    count = 0
    while count < 6:
        lottoNum = random.randint(1,49)
        if lottoNum not in lottoLst:
            lottoLst.append(lottoNum)
            count += 1
    lottoLst.sort()
    print(lottoLst)

def main():
    for i in range(1,6):
        lotto()

main()