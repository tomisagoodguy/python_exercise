'''
7.	自行輸入兩個辭典，以輸入值end作為結束，將這兩個辭典合併，
根據key值字母，由小到大排序輸出，如有重複key值，後輸入的key值覆蓋前面的key值。
'''
def inpDic(dic):
    while True:
        key = input("Key:")
        if key == "end":
            break
        else:
            value = input("Value:")
            dic[key] = value
    return dic

#==============================================
dic1 = {}
dic2 = {}
print ("Create dic1")
dic1 = inpDic(dic1)

print ("Create dic2")
dic2 = inpDic(dic2)

dic = dic1.copy()
dic.update(dic2)
lit = sorted(dic)

for i in lit:
    print("%s:%s"%(i,dic[i]))
