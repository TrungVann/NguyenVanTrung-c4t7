from turtle import *
speed = 0
n = int(input("so canh: "))

a= 360/n
for _ in range(n):
    forward(100)
    left(a)
    n = n + 1



mainloop()