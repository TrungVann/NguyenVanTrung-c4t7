from turtle import *
n = int(input("so hinh: "))

a = 3

for j in range(n):
    for i in range(a):
        forward(100)
        left(360/a)
    a = a +1

mainloop()