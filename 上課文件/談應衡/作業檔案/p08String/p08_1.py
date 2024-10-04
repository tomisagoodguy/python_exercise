import os
os.system('cls')
#建立空字串
s1 = str()
s2 = ""
# print('s1=',s1,'s2=',s2)

#初始值
s3 = 'Learning Python now!'
s4 = str(28721940)
s5 = s3 + s4
print('s3 = ',s3,'\ns4 = ',s4)
# print('s5=',s5)
# print()
#字串運作
'''
#字串長度、最大、最小
a = len(s5)
b = max(s5)
c = min(s4)
print('s3字串長度:',a,'\n字串內最大值:',b,'\n字串內最小值:',c)

'''
#索引運算子 []
'''
a = s3[3]
b = s3[-1]
c = s3[-6]
# print ('字串中索引值3的字元:',a,'\n索引值-1的字元:',b,'\n索引值-6的字元:',c)

#分割運算子[start:end]
a = s3[8:15]
b = s3[:8]
c = s3[16:]
print('索引值a [8:15]:',a)
print('索引值b [:8]:',b)
# print('索引值c [8:]:',c)
'''

'''
#檢視字串是否存在指定內容 in ; not in
L1 = a in s3
L2 = b not in s3
print('L1:',L1, '\nL2:',L2)
'''

#連結與複製
'''
d = b +' '+ a + " " + c
print ("d=",d)
d = d * 2
print ("d=",d)

# A = ('633','665','998','772','443')
# print(' + '.join(A) + " = ",end = "")         #將"+"與tuple內容串接
# print(eval('+'.join(A)))                #將"+"與tuple內容串接並計算

#=========簡單的加法命題=================
# import random
# x = [str(i) for i in range(1,1000)]
# X = random.choices(x,k =3)
# # print(X)
# print(' + '.join(X) + " = ",end = "") 
# Y = eval('+'.join(X))
# # print(Y)

# A = int((input("")))

# if A==Y:
#     print("答對了!!")
# else:
#     print("答錯了!!")


#將字串內容轉換為ASCII整數
# a = ord(s3[4])
# print(f"{s3[4]} 的ASCII碼為 {a}")

# #將ASCII整數內容轉換為字串
# m=chr(a)
# print(f'ASCII {a}是 字母 {m}')

'''

#列印字串所有字元(逐一顯示)
'''
for i in s4:
    print(i,end=' ')
print()

for i in range (len(s4)):
    print(s4[i],end=' ')
'''

#子字串相關功能
'''
s5 = s5*2
print("\ns5=",s5)
k = "now!"
a = s3.endswith(k)  #字串最後是否為"now!"
b = s3.startswith('Learning')   #字串最前面是否為'Learning'
c = s5.find('Learning')    #尋找第一個出現的Learning
d = s5.rfind('Learning')   #尋找最後一個出現的Learning
e = s5.count('n')   #計算n的數量
print(f'字串最後是否為"now!"：{a},\n字串最前面是否為"Learning"：{b}')
print(f'第一個出現的 Learning：{c},\n最後一個出現的 Learning：{d},\n共 {e} 個 n')
'''

#測試字串
'''
s5 = 'John0123'
print('s5=',s5)
print()
a = s3.isalnum()
b = s5.isalnum()
print(f'英數字元組合 s3:{a} s5:{b}')

a = s3.isalpha()
b = s5.isalpha()
print(f'英文字母組合 s3:{a} s5:{b}')

a = s3.isdigit()
b = s4.isdigit()
print(f'數字組合 s3:{a} s4:{b}')

s1 = 'abcde'
s2 = 'ABCDE'
a = s1.islower()
b = s2.islower()
c = s1.isupper()
d = s2.isupper()
print(f' s1 is lower:{a}\n s2 is lower:{b}\n s1 is upper:{c}\n s2 is upper:{d}')

s2 = "     "
c = s2.isspace()
print (f"空白字元 s2:{c}")

a = input("識別字：")
print(a.isidentifier())   #判斷字串是否可作為合法的識別字
'''

#轉換字串
'''
s3 = s3.replace('Python','Python_Ver3.10')# 改換字串
print(s3)
s3 = s3.lower()  #字串全部改為小寫
print(s3)
s3 = s3.upper()  #字串全部改為大寫
print(s3)
s3 = s3.capitalize()  #第一個字元改為大寫，其他改為小寫
print(s3)
s3 = s3.title() #字串內每個單字第一個字母大寫
print(s3)
s3 = s3.swapcase() #字串內所有大小寫交換
print(s3)

#===更換第一個字母為大寫====
id = input("身份證字號：")
id = id.capitalize()
print(id)
'''

#去頭尾空白
'''
s3 = " "+ s3 + " "
print(s3+'.')
s3 = s3.lstrip()
print(s3+'.')
s3 = " "+ s3 + " "
s3 = s3.rstrip()
print(s3+'.')
s3 = " "+ s3 + " "
print(s3+'.')
s3 = s3.strip()
print(s3+'.')
'''
#字串對齊模式
# '''
print(s4+'.')
# print(f"{s4:15}"+".")   #僅在排版顯示空白
# print(s4+".")
# print("字串s4長度為：",len(s4))
# s4 = s4.center(10)
# print(s4+'.')
# print("字串s4長度為：",len(s4))
# s4 = s4.ljust(15)       #將空白字元加到變數中 
# print(s4+'.')
# s4 = s4.rjust(20)
# print(s4+'.')
# '''

#分割字串
'''
s1 = '2019/10/20'
s2 = '02-28721940-262'
s3 = '蘋果 香蕉 柿子 西瓜'
s4 = '趙一,錢二,孫三,李四'
lst1 = s1.split('/')
lst2 = s2.split('-')
lst3 = s3.split()
lst4 = s4.split(',')
print('lst1 = ',lst1)
print('lst2 = ',lst2)
print('lst3 = ',lst3)
print('lst4 = ',lst4)

s5 = "23\n12\n45\n56"
# print(s5)
lst5 = s5.splitlines()
print('lst5 = ',lst5)
s6 = "23\n12\n45\n56"
# print(s6)
lst6 = s6.split("\n")
print('lst6 = ',lst6)

'''
