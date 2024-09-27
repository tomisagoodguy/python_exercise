'''
7	撰寫一個程式：
7.1	以迴圈方式，提供使用者反覆輸入西元年分，直到輸入999結束。
7.2	判斷輸入年份是否為閏年。判斷規則為，每4年一閏，100年不閏，但400年也一閏

'''
while True:
    year = int (input("請輸入西元年："))
    
    if year == 9999:
        break

    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("%d年是閏年" %year)

    else:
        print("%d年不是閏年" %year)
print("程式結束")