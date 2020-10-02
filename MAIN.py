s = open("data.txt", "a")#opens text file
lift = input("enter lift: ")#lets user enter exercise
mass = int(input("enter mass (KG):"))#lets user enter mass
setcount = int(input("enter num of sets "))#lets user enter set number
s.write(str(lift)+":"+"\n"+str(mass)+"KG"+"x")#writes lift and mass and line break to file
s.close#closes txt file
currentset = 1#decares current set as variable
while currentset < setcount:#compares current set to user entered set
    comp = input("press any key to start next set")#lets user go through sets
    currentset = currentset + 1# adds one to current set
    print("you are on set "+str(currentset))#prints current set
    if currentset == setcount:#checks if you have completed the sets
        print("Good job! you done!")#prints nic emssaghe :)
        s = open("data.txt", "a")#opens txt file
        s.write(str(setcount))#saves setcount to files
        s.close()#closes txt file
        break#not sure if this does anything lol so ill keep it in case
    else:#most likely not needed too lazy to check
        pass#most likely not needed too lazy to check
