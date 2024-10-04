'''
8.	輸入顏色辭典color_dict 內容，直到鍵值輸入end為止。再依據鍵值字母由小到大排序輸出
'''
dic = {}

while True:
    key = input("Key:")
    if key == "end":
        break
    else:
        value = input("Value:")
        dic[key] = value

dics = sorted(dic)
print(dics)
for i in dics:
    print("%s:%s"%(i,dic[i]))