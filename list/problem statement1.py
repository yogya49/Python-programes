'''wrie a python code to give list as user input
add conformed guests to a list
remove the guest who cancels
check if the guest is present in the party
sort and print the final guest list'''
guests=[]
while (True):
    print("*******menu*******")
    print("1.add the guest...")
    print("2.remove the guest who cancels..")
    print("3.check if the guest is attending the party..")
    print("4.view the final guest list..")
    print("5.exit..")
    print("..............................")
    choice=int(input("enter your choice:"))
    if(choice>=1 and choice<=5):
        if(choice==1):
            guest_name=input("add the guest:")
            guests.append(guest_name)
            print(f"{guest_name} is added to the guests.. ")
        elif(choice==2):
            cancelled_guest=input("the cancelled guest is:")
            if cancelled_guest in guests:
                guests.remove(cancelled_guest)
                print(f"{cancelled_guest} is removed from guests.. ")
            else:
                print(f"{cancelled_guest} is not in the list..")
        elif(choice==3):
            check_guest=input("enter the guest name to check..")
            if check_guest in guests:
                print(f"{check_guest} is attending the party..")
            else:
                print(f"{check_guest} is not attending the party..")
        elif(choice==4):
            guests.sort()
            print(f"these atr the final guests coming to the party {guests}")
        else:
            print("thank you.....")
            break






