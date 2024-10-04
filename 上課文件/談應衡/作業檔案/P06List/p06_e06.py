'''
2.11.6	使用者輸入十個數字，做為樣本數，輸出眾數(出現最多次數的數字)
'''
sample = []
count = [0]*10

for i in range(len(count)):
    num = int (input('Input integer:'))

    sample.append(num)
    a = sample.index(num)   #找出輸入的值是否曾經出現過，出現的索引值位置
    count[a] = count[a]+1          #將相同位置的count索引值加1

num_occu = max(count)       #找出count[]中最大的值

print(sample[count.index(num_occu)]) #索引count[]最大值的所在位置，對應sample[]的內容
print(num_occu)


