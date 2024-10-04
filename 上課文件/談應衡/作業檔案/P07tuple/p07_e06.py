'''
6.	課程分組，分為X與Y兩組，輸入X和Y兩組需要學習的科目到集合中，以字串”end”作為結束，請依序分行顯示
(1)	X組和Y組所有的科目
(2)	X組和 Y組共同科目
(3)	Y組有但是X組沒有的科目
(4)	X和Y組都沒有的科目 (題目描述有誤，應改為"X組沒有或Y組沒有的所有科目")
(5)	X組: 國文、英文、數學乙、地理、歷史。 Y組：國文、數學甲、英文、物理、化學
'''

def inpSet(setn):
    while True:
        n = input("輸入科目名稱(輸入end結束)：")
        if n == "end":
            break
        else:
            setn.add(n)
    return setn

X = set()
Y = set()

print("X組課程科目")
X = inpSet(X)

print("Y組課程科目")
Y = inpSet(Y)
# X= {'國文','英文','數學乙','地理','歷史'}
# Y= {'國文','數學甲','英文','物理','化學'}

A = (X|Y)
B = (X&Y)
C = (Y-X)
D = (X^Y)
print ("X組和Y組所有的科目：",A)
print ("X組和 Y組共同科目：",B)
print ("Y組有但是X組沒有的科目",C)
print ("X和Y組對方沒有的科目：",D)