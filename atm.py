cash=int(input("enter amount you want to withdraw:"))
notes_denom=(2000,500,200,100,50,20,10,5,2,1)
# unchangeble tuple
print("select denomination:")
counter=0

while cash > 0:
    print("do you want %d Y/N...?"%notes_denom[counter],end=" ")
    resp = input()
    response = resp[0].upper()
    if response == "Y":
        notes = cash//notes_denom[counter]
        cash %=notes_denom[counter]
        print("{} =>{}".format(notes_denom[counter],notes))
        counter += 1
    else:
        counter += 1