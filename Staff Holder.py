print("Welcome to Staff-Holder Made by Umang Singh")
print("Here we have all imformation about any staff....")
password = int(input("Enter Shop Password - "))
if password == 2587:
    print("Access Granted")
else:
    print("Access Denied")
    exit()
sname = int(input("Enter Staff No. : "))
if sname == 1:
    print("Staff Name : Umang Singh \n Joined-2 march 2020 \n He is working in the shop")
if sname == 2:
    print("Staff Name : Rajat Singh \n Joined-25 april 2021 \n He is working in the shop")
if sname == 3:
    print("Staff Name : Kalash Singh\n Joined-26 march 2022 \n He is not working in the shop")
if sname == 4:
    print("Staff Name : Rahul Singh \n Joined-29 april 2023 \n He is working in the shop")
if sname == 5:
    print("Staff Name : Pramod Singh \n Joined-30 may 2023 \n He is not working in the shop")
