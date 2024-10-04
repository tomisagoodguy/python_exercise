'''
9.	輸入資料到字典中，直到輸入鍵值為end結束，再輸入一個鍵值，進行搜尋這個鍵值是否存在字典中。
'''
dic = {}

while True:
    key = input("Key:")
    if key == "end":
        break
    else:
        value = input("Value:")
        dic[key] = value

print()

search = input ("search key: ")
a = search in dic
print(a)
