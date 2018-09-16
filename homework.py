print ("hi there, this is a superuser gateway")
username = input("enter username: ")

if username == "techkids": #check username
    password = input("enter password: ") #nhập password
    if password == ("codethechange"): #check password
        print ("welcome, techkids")
    else:
        print ("password is incorrect")
else: # nếu username sai
    print ("you are not superuser")