# 3/27/2024
# Program that stores passwords

password = input("create a password? ")

#def view():
with open('password.txt','r+')as f:
       for i in password():
           f.write(password)
    

def add():
    name = input('Account Name:')
    pwd = input("Password:")
    with open('passwords.txt', 'a')as f:
        f.write(name + "|" + password + "\n")
while True:
    mode = input(
        "Would you like to add a new password or view existing ones (view, add), press q to quit? ").lower()
    if mode == "q":
        break
    #elif mode == "view":
        #view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue