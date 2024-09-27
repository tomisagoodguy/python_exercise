'''
1.	建立一個函式compute()，讓使用者輸入學號、姓名、科系，透過呼叫顯示這些訊息。
'''
s = "輸入學生資料"      #全域變數
def compute():      #定義函式名稱
    print(s)
    stu_id = input("學號：")
    stu_name = input("姓名：")
    stu_dept = input("科系：")

    print("===========\n科系：",stu_dept)
    print("學號：",stu_id)
    print("姓名",stu_name)

compute()       #呼叫函式及執行

#=========使用return返傳結果===========
# def compute():
#     stu_id = input("學號：")
#     stu_name = input("姓名：")
#     stu_dept = input("科系：")
#     S = "===========\n學號："+stu_id+"\n姓名："+stu_name+"\n科系："+stu_dept
#     return S

# Str = compute()
# print(Str)