# 3.使用者輸入一個句子，(至少五個詞，以空白隔開，並輸出倒數三個詞)
#想不出要輸入甚麼可用範例句： It is better to learn a certain trade than to possess a large fortune. 

S = input("輸入一句話：")
lst = S.split()  #以空白分割字串後將單字存放到串列內
# print(lst) #檢視串列內容

print(' '.join(lst[-3:])) #由後往前算第3個空白到最後所有的字合併輸出為新的字串
