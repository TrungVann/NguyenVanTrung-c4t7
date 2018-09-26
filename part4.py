
username = input("enter your username: ")
password = input("enter your password: ")
email = input ("enter your email: ")
while "@" not in email:
    print("your email wrong")
    email = input ("enter your email: ")
n = input("enter your password again:")
if password == n:
    print(" ")
else:
    print ("please enter your password again ")
    n = input("enter your password again:")
print ("welcome")
print ("nick mới của bạn đã hoàn thành")
