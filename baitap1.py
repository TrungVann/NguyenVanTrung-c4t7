# print ("* * * * * * * * * * * * * * * * * * * * ")

# i = int(input("so sao: "))
# for i in range(0, i):
#    print ("*", end = " ")

# print (" x *"*4 , end = " x")

# a = int(input("tong cong: "))
# print (" x *"*a, end = " x")

# for i in range(0,3):
#     print ("*"*7, end = "")
#     print ()

# n = int(input("dòng: "))
# m = int(input("sao: "))
# for i in range (0,n):
#     print("*"*m, end = " ")
#     print ()

x = 2 
y = 3
for i in range (0,5):
    for j in range (6):
        if i == y and j == x:
            print("*", end = " ")
        else:
            print("-", end = " ")
    print ()