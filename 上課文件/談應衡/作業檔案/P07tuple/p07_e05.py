'''
5.	依序輸入五個、三個、九個整數，儲存到set1、set2、set3當中，
查詢set2是否為set1的子集合?set3是否為set1的超集合?
'''
def inpSet(a,setn):
    for i in range(a):
        n = int(input("Enter an integer:"))
        setn.add(n)
    return setn

set1 = set()
set2 = set()
set3 = set()

print("Input to set1:")
set1 = inpSet(5,set1)

print("Input to set2:")
set2 = inpSet(3,set2)

print("Input to set3:")
set3 = inpSet(9,set3)

print(set1)
print(set2)
print(set3)

s2 = set2.issubset(set1)
if s2 == True:
    s2 = "yes!"
else:
    s2 = "no!"
s3 = set3.issuperset(set1)
if s3 == True:
    s3 = "yes!"
else:
    s3 = "no!"

print("set2 is subset of set1:",s2)
print("set3 is superset of set1:",s3)