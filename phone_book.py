# Amanda M
# 3/27/2024
#Continuation of last weeks programs
#Multi-Dimensional Array
# All of this is stored in an array so try throwing this into coolfile.py or make it a file
names = []
phone_number = []
addy = []

num = 1

for i in range(num):
    name = input("Enter Name: ") 
    phone_num = input("Enter Phone Number: ")
    address = input("Enter email address: ")

    names.append(name)
    phone_number.append(phone_num)
    addy.append(address)

print("\tNAME\t\t\tPHONE NUMBER\t\t\tEMAIL")

for i in range(num):
    print(f"\t{names[i]}\t\t\t{phone_number[i]}\t\t\t{addy[i]}")
# I stopped here adding email address

s = input("Enter the Name to Search: ")
if s in names:
    index = names.index(s)
    names = names[index]
    phone_number = phone_number[index]
    addy = addy[index]
    print(f"Name: {names}, Phone: {phone_number}, Email Address: {addy}")
else:
    print("Name not found!")

# Figure out how to add email and a loop so user will be prompted w/o help from admin