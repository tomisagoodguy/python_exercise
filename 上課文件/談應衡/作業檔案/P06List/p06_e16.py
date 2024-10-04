def output(aList):
    for i in range(len(aList)):
        aList[i] = eval(input('輸入5個整數：'))
    return aList

def max(aList):
    maxNum = aList[0]
    for i in range(len(aList)):
        if aList[i] > maxNum:
            maxNum = aList[i]
    return maxNum

def min(aList):
    minNum = aList[0]
    for i in range(len(aList)):
        if aList[i] < minNum:
            minNum = aList[i]
    return minNum

def main():
    lst = [0]*5
    print(output(lst))
    print('Max = ',max(lst))
    print('Min = ',min(lst))

main()