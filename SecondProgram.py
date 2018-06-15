print("List Functions")
print("1: length")
print("2: append")
print("3: copy")
print("4: insert")
print("5: index")
print("6: pop")
print("7: count")

size=int(input("Enter the size of list"))
l=[]
for i in range(0,size):
    x = input("Enter the value")
    l.append(x)

print("The list is",l)


while 1:
    print("::::::::::::::::::::::::::::::::")
    print("Which function u want to perform")
    print(":::::::::::::::::::::::::::::::::")
    ch = input()
    if ch=="1":
        print("Length of a list is:",len(l))
    elif ch=="2":
         a=input("Enter what you want to append")
         l=l.append(a)
         print("after append the list is:  ",l)

    elif ch=="3":
        a.copy(l)
        print(a)
    elif ch=="4":
        a=input("enter what u want to insert")
        l.insert(a)
        print(1)
    elif ch=="5":
        print(l.index(size))
    elif ch=="6":
        pop(l)
    elif ch=="7":
        l.count()
    else:
        pass
    print("Do u want to continue: yes/no ")
    a=input()
    if a=="yes":
        continue
    else:
        break
