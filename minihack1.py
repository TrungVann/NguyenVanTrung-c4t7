#1
kho = {
    'hp' : 20,
    'dell' : 50,
    'macbook' : 12,
    'asus' : 30
}
#2
print("macbook", kho['macbook'])
print()
#3
user_ans = input("muốn biết về máy nào: ")
user_ans = user_ans.lower()
if user_ans in kho.keys():
    print("còn", kho[user_ans], "loại máy đó.")
else:
    print("không có máy đó")
#4
kho['toshiba'] = 10
print("Đã bổ sung thêm Toshiba vào kho")
print()
#5
user_ans_may = input("nhập tên máy muốn thêm ")
user_ans_may = user_ans_may.lower()

if user_ans_may in kho.keys():
    print("Đã tồn tại")
else:
    user_ans_soluong = int(input("số: "))
    kho[user_ans_may] = user_ans_soluong
    print("thêm thành công")
#6
kho['dell'] += 10
kho['macbook'] -= 2