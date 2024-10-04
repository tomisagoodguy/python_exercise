'''
2.11.4	隨機輸出五張撲克牌，不論花色，計算點數
'''
import random
cards = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']
tol = 0

for i in range(0,5):
    a = random.choice(cards)
    print(a,end = ' ')
    if a == 'A':
        a = 1
    elif a == 'J':
        a = 11
    elif a == 'Q':
        a = 12
    elif a == 'K':
        a = 13
    tol += a

print ('\n%d'%tol)