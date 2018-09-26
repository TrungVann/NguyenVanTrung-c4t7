m = int(input("enter a month:"))
0 < m <= 12
if m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or m == 12:
    print("so ngay: 31")
elif m == 2:
    print("so ngay: 28 (neu nam nhuan thi se la 29")
else:
    print ("so ngay: 30")