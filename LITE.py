import time
import random
motiv = ["YOU GOTTA GET THE JUICE!","COME ON!, MORE ENERGY"]
congrats = ["POGGERS","THE BREAD HAS BEEN GOTTEN", "YOU GOT THE JUICE"]
bye = ["GOODBYE WARLORD", "CYA SOON", "GG EZ"]
saves = 1#dont know what this does or wahy its called saves lol




def new_lift_main_loaded(): #runs if you load save
    saves = 1#dont know what this does or wahy its called saves lol
    lift = input("enter lift: ")#lets user enter exercise
    mass = int(input("enter mass (KG):"))#lets user enter mass
    reps=input("how many reps? ")
    setcount = int(input("enter num of sets "))#lets user enter set number
    currentset = 1#decares current set as variable
    while currentset < setcount:#compares current set to user entered set
        comp = input("press any key to start next set")#lets user go through sets
        currentset = currentset + 1# adds one to current set
        print("you are on set "+str(currentset))#prints current set
        if currentset == setcount:#checks if you have completed the sets
            print(random.choice(congrats))#prints nic emssaghe :)
            from saveload import date#brings date variable into the file
            s = open("%s.txt" % date, "a")#opens text file
            s.write(str(lift)+":"+"\n")
            if saves < setcount:
                s.write(str(mass)+"x"+str(reps)+"\n")#saves setcount to files MAKE THIS DO IT SET times
                saves = saves + 1
            stop = input("CONTINUE TRAINING? ")
            if stop == "y":
                KEEPGOING()
                s.close()
            else:
                print(random.choice(bye))
                s.close()
            
           
        
 
    
            

def new_lift_main_fresh(): #runs if you start fresh
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
            print(random.choice(congrats))#prints nic emssaghe :)
            s = open("%s.txt" % date, "a")#opens text file
            s.write(str(lift)+":"+"\n")
            while saves < setcount:
                s.write(str(mass)+"x"+str(reps)+"\n")#saves setcount to files MAKE THIS DO IT SET times
                saves = saves + 1
            stop = input("CONTINUE TRAINING? ")
            if stop == "y":
                KEEPGOING()
                s.close()
            else:
                print(random.choice(bye))
                s.close()
            
 



        








def BESTCODERKEKW():
    doyouwanttosave = input("do you want to load a save file? ")#lets you load save
    if doyouwanttosave.lower() == "y":
        import saveload
        new_lift_main_loaded()
    
    else:
        global date
        date = input("enter date eg  (2.10.20) ")
        s = open("%s.txt" % date, "a")#opens text file
        new_lift_main_fresh()
        
def KEEPGOING():
        global date
        date = date
        s = open("%s.txt" % date, "a")#opens text file
        new_lift_main_loaded()
      



print(random.choice(motiv))
BESTCODERKEKW()


