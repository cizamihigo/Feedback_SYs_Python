import sqlite3
# import hashlib
con = sqlite3.connect("Logins.db")
coCur = con.cursor()

# coCur.execute("CREATE TABLE Log(Id INTEGER PRIMARY KEY AUTOINCREMENT, UserName VARCHAR(50) NOT NULL, Password VARCHAR(255) NOT NULL, UserType VARCHAR(2) DEFAULT 'U')")
def add_user():
    print("ADDING NEW USER FORM")
    print("********************")
    UserName = input("Enter your Username: (@fulani):\t")
    Password = input("Enter User Password:           \t")
    if usertype == 'S':
        Nusertype = input("Enter a user Type: ('U','A','S'):\t")
        if len(UserName) < = 50 and len(Password) < = 200 and len(Nusertype) < 2 and ( Nusertype='S' or Nusertype = 'A' or Nusertype = 'U'):
            cosel = con.cursor()
            cosel.execute("SELECT UserName FROM Log WHERE Username = ?",[UserName])
            selet = cosel.fetchall()
            if selet[0] == []:
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
        if len(UserName) < 51 and len(Password) < 201 and len(Nusertype) < 2:
            cosel = con.cursor()
            cosel.execute("SELECT UserName FROM Log WHERE Username = ?",[UserName])
            selet = cosel.fetchall()
            if selet[0] == []:
                coCur.execute("INSERT INTO Log(UserName, Password) VALUES(?,?)",(UserName,Password))
                con.commit()
                print("\t\t\t\t\tUSer Added Successfully!")
            else:
                print("User Name Already registered in our Database. Please choose another one.")
        elif len(UserName) > 50:
            print("This Username Is to long to remember Choose a simple one")
    con.close()
    coCur.close()
    cosel.close()

def login():
    Name = input("Enter Your UserName: \t")
    Password = input("Enter Your Password:\t",NotImplemented)
        