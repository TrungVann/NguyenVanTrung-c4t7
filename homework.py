#1
# list_rỗng = []
# print (list_rỗng)

# 2
# a = ["LOL"]
# print (a)

#3
b = ["LOL", "BTS", "Sport"]

#4
new_b = "TECHKIDS"
b.append(new_b)
print (b)

#5
# b.append(input("enter somethings: "))
# print (b)

#6: print (*b, sep = " ")

#7: print (*b, sep = ", ")

#8
# print (*b, sep = "|")

#9
# print (b[0], b[-1])

#10
#print (b[0], b[-1], b[-2])

#11
# b[0] = "Deadpool"
# print(b)

#12
# b[-1] = "dragon ball"
# print (b)

#13
# vi_tri = int(input("Nhap vi tri phan tu ban muon thay the "))
# thay_the = input("Ban muon thay no thanh gi ")
# b[vi_tri] = thay_the
# print (b)

#14
# b.pop (1)
# print(b)

#15
# if "LOL" in b:
#   b.remove("LOL")
#   print (b)
# else:
#   print("LOL khong ton tai")

#16
# vi_tri = int(input("Nhap vi tri phan tu "))
# if vi_tri < len(b):
#   b.pop(vi_tri)
#   print(b)
# else: 
#   print("ko ton tai phan tu")

#17
# gia_tri = input("Nhap gia tri phan tu ban muon xoa ")
# if gia_tri in b:
#   b.remove(gia_tri)
#   print(b)
# else:
#   print("Khong ton tai gia tri")

# #18,19
# b.insert(1, "HAHA")
# b.append("HHOHO")
# b.insert(4, "HIHI")
# print (b)
# for item in b:
#     print(item)

#20 
b.insert(1, "HAHA")
b.append("HHOHO")
b.insert(4, "HIHI")
for i, item in enumerate(b):
    item = item.upper()
    print(i + 1, item)