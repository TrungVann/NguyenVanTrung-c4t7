dict_rong = {}
dict_1capkv = {"Ten": "Nguyen Van Trung"}
dict_2capkv = {
    "Ten": "Nguyen Van Trung",
    "Lop": "c4t7"
}

nhanvat = {
    "Name": "Tom",
    "đặc điểm" : "con mèo đi bằng 2 chân",
    "màu lông" : "Xanh"
}
# bài 5
print (nhanvat)
nhanvat["sở thích"] = "bắt chuột"
print (nhanvat)

# bài 6
print (nhanvat)
key_mới = input("key nhập vào: ")
value_mới = input ("value nhập vào")
nhanvat[key_mới] = value_mới
print (nhanvat)

# bài 7
print (nhanvat["Name"],",", nhanvat["đặc điểm"])

# bài 8
print(nhanvat)
key_mới = input("key nhập vào: ")
print (nhanvat[key_mới])

# bài 9,10
a = input("đặc điểm mới: ")
nhanvat["đặc điểm"] = a
print(nhanvat)

# bài 11,12
b = input("key muốn xoá: ")
del nhanvat[b]
print (nhanvat)

#bài 13
c = input("key muốn kiểm tra: ")
if c in nhanvat:
    print ("True")
    print (c, "exists in my dicionary")
else:
    print ("False")
    print (c, "does not exists in my dictionary")

# baì 14
word = {"Name language": "English",
    "Particular" : """ a West Germanic language that was first spoken in early medieval England
    and is now a global lingua franca. Named after the Angles,
    one of the Germanic tribes that migrated to the area of Britain that would later take their name,
    England, both names ultimately deriving from the Anglia peninsula in the Baltic Sea. 
    It is closely related to the Frisian languages, 
    but its vocabulary has been significantly influenced by other Germanic languages, 
    particularly Norse (a North Germanic language), as well as by Latin and French."""
}
print (word)

# bai 15,16
word["hello"] = "hi, xin chào"
word["raichu"] = "1 con pokemon, chi tiết => google"
word["learn"] = "same meaning with study, học"
d = input("enter a word: ").lower()
if d in word:
    print(word[d])
else:
    print ("sorry hihi")

