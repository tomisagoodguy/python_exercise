'''
3.	輸入至少五個字串至數組，直到輸入’end’結束，接著輸出這個數組，
再分別顯示數組的第一個元素到第三個元素，和倒數第三個元素。
'''
tup = ()

while True:
    word = input("Enter a word:") #輸入字串
    if word == "end":
        break           # 輸入 end 結束
    else:
        tup += (word,)

print(tup)          #輸出數組
print(tup[0:3])     #輸出數組的第一個元素到第三個元素
print(tup[-3])     #輸出數組的倒數第三個元素
