import time
global saves
saves = 1#dont know what this does or wahy its called saves lol
def new_lift_main_loaded(): #runs if you load save

    lift = input("enter lift: ")#lets user enter exercise
    mass = int(input("enter mass (KG):"))#lets user enter mass
    reps=input("how many reps? ")
    setcount = int(input("enter num of sets "))#lets user enter set number
    #s.write(str(lift)+":"+"\n"+str(mass)+"KG"+"x")#writes lift and mass and line break to file
    #s.close#closes txt file
    currentset = 1#decares current set as variable
    while currentset < setcount:#compares current set to user entered set
        comp = input("press any key to start next set")#lets user go through sets
        currentset = currentset + 1# adds one to current set
        print("you are on set "+str(currentset))#prints current set
        if currentset == setcount:#checks if you have completed the sets
            print("Good job! you done!")#prints nic emssaghe :)
            from saveload import date#brings date variable into the file
            s = open("%s.txt" % date, "a")#opens text file
            s.write(str(lift)+":"+"\n")
            while saves < setcount:
                s.write(str(mass)+"x"+str(reps)+"\n")#saves setcount to files MAKE THIS DO IT SET times
                saves = saves + 1
            s.close()#closes txt file
            pass
            break#not sure if this does anything lol so ill keep it in case
        else:#most likely not needed too lazy to check
            pass#most likely not needed too lazy to check

def new_lift_main_fresh(): #runs if you load save
    global saves
    lift = input("enter lift: ")#lets user enter exercise
    mass = int(input("enter mass (KG):"))#lets user enter mass
    reps=input("how many reps? ")
    setcount = int(input("enter num of sets "))#lets user enter set number
    #s.write(str(lift)+":"+"\n"+str(mass)+"KG"+"x")#writes lift and mass and line break to file
    #s.close#closes txt file
    currentset = 1#decares current set as variable
    while currentset < setcount:#compares current set to user entered set
        comp = input("press any key to start next set")#lets user go through sets
        currentset = currentset + 1# adds one to current set
        print("you are on set "+str(currentset))#prints current set
        if currentset == setcount:#checks if you have completed the sets
            print("Good job! you done!")#prints nic emssaghe :)
            s = open("%s.txt" % date, "a")#opens text file
            s.write(str(lift)+":"+"\n")
            while saves < setcount:
                s.write(str(mass)+"x"+str(reps)+"\n")#saves setcount to files MAKE THIS DO IT SET times
                saves = saves + 1
            s.close()#closes txt file
            pass
            break#not sure if this does anything lol so ill keep it in case
        else:#most likely not needed too lazy to check
            pass#most likely not needed too lazy to check



        








        
print("REMEMBER PYTHON COUNTS FROM 0")
time.sleep(1)
print("so add +1 on set number")
time.sleep(1)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
time.sleep(0.5)
print("----------------------------------------------------------")
time.sleep(0.5)
wlc=open("welcome.txt", "r")
file_contents = wlc.read()
print(file_contents)
print("----------------------------------------------------------")
doyouwanttosave = input("do you want to load a save file? ")#lets you load save
if doyouwanttosave.lower() == "y":
    import saveload
    new_lift_main_loaded()

else:
    date = input("enter date eg  (2.10.20) ")
    s = open("%s.txt" % date, "a")#opens text file
    new_lift_main_fresh()








time.sleep(10000)

#HAS WEIRD BUG WHERE IT OPENS THE SAVE/LOAD AFTE FIRTS CYCLE?? PLZ FIX LUL




        
