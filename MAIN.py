s = open("data.txt", "a")
lift = input("enter lift: ")
mass = int(input("enter mass (KG):"))
setcount = int(input("enter num of sets "))
s.write(str(lift)+":"+"\n"+str(mass)+"KG"+"x")#writes lift and mass and line break to file
s.close
currentset = 1
while currentset < setcount:#compares current set to user entered set
    comp = input("press any key to start next set")
    currentset = currentset + 1
    print("you are on set "+str(currentset))
    if currentset == setcount:
        print("Good job! you done!")
        s = open("data.txt", "a")
        s.write(str(setcount))
        s.close()
        break
    else:
        pass
