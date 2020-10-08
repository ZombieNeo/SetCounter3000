#load save
def save_system():
    doload = "y"
    if doload == "y" or "Y":
        global date
        date= input("enter save name (date) ")
        s = open("%s.txt" % date, "a")
        print("LOADED SUCCESSFULLY")
        pass
    else:
        pass
    
save_system()
