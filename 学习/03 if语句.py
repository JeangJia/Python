username = "Jeang"
password = 1900
inpUsername = input("username:")
inpPassword = input("password:")
if username == inpUsername and password == inpPassword:
    print("login success")
elif username == inpUsername and password != inpPassword:
    print("password error")
else:
    print("login failed")
