import sqlite3
import getpass
# import hashlib
con = sqlite3.connect("Logins.db")
coCur = con.cursor()

# coCur.execute("CREATE TABLE Log(Id INTEGER PRIMARY KEY AUTOINCREMENT, UserName VARCHAR(50) NOT NULL, Password VARCHAR(255) NOT NULL, UserType VARCHAR(2) DEFAULT 'U')")
def add_user(usertype):
    print("ADDING NEW USER FORM")
    print("********************")
    UserName = input("Enter your Username: (@fulani):\t")
    Password = getpass.getpass(prompt="Enter User Password:           \t") #input("")
    if usertype == 'S':
        Nusertype = input("Enter a user Type: ('U','A','S'):\t")
        if len(UserName) <  51 and len(Password) < 201 and len(Nusertype) < 2 and ( Nusertype =='S' or Nusertype == 'A' or Nusertype == 'U'):
            cosel = con.cursor()
            cosel.execute("SELECT UserName FROM Log WHERE Username = ?",[UserName])
            selet = cosel.fetchall()
            if selet == []:
                coCur.execute("INSERT INTO Log(UserName, Password, UserType ) VALUES(?,?,?)",(UserName,Password,Nusertype))
                con.commit()
                print("\t\t\t\t\tUSer Added Successfully!")
            else:
                print("User Name Already registered in our Database. Please choose another one.")
        elif len(UserName) > 50:
            print("This Username Is to long to remember Choose a simple one")
        elif len(Nusertype) > 2 or (Nusertype != 'S' or Nusertype != 'A' or Nusertype != 'U' ):
            print("User type should only be  S or U or A :\t")
    else:
        Nusertype = 'U'
        if len(UserName) < 51 and len(Password) < 201 and len(Nusertype) < 2:
            cosel = con.cursor()
            cosel.execute("SELECT UserName FROM Log WHERE Username = ?",[UserName])
            selet = cosel.fetchall()
            if selet == []:
                coCur.execute("INSERT INTO Log(UserName, Password) VALUES(?,?)",(UserName,Password))
                con.commit()
                print("\t\t\t\t\tUSer Added Successfully!")
            else:
                print("User Name Already registered in our Database. Please choose another one.")
        elif len(UserName) > 50:
            print("This Username Is to long to remember Choose a simple one")
    # con.close()
    # coCur.close()
    # cosel.close()

def login():
    Name = input("Enter Your UserName: \t")
    Password = getpass.getpass(prompt="Enter User Password: \t") 
    conn = sqlite3.connect('Logins.db')
    cue = conn.cursor()
    cue.execute("SELECT * FROM Log WHERE UserName = ? AND Password = ?",(Name, Password))
    vcue = cue.fetchall()
    if vcue == []:
        print("No such User In our Databse Please Sign Up first")
        print("Do you Want To Sign Up (Y) or (N) 1 or 0: ")
        signup = input("\t")
        if signup == 'Y' or signup == 'y' or signup == int('1') or signup == '1':
            add_user(usertype='U')
        elif signup == 'N' or signup == 'n' or signup == int('0') or signup == '0':
            print("Good Bye!!!!!\n\n")
            quit()
        else:
            print("SIGNIN AGAIN\n*************")
            log = input("Do you want to login once again? Y or N")
            if log == 'Y' or log == 'y':
                login()
            else:
                print("Not a choice! Good Bye!")
                quit()
    else:
        print(vcue)
        login.var = "{0}".format(vcue[0][1])
        login.varu ='{0}'.format(vcue[0][3])
        print("WELCOME USER. Your personal info are such: \nUsername = {0}\nUser Type = {1}".format(vcue[0][1],vcue[0][3]))
        