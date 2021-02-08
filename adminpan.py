import sqlite3
import logins
def admin():
    print("ADMIN PANEL\n****************")
    print("\
        1. Add users\n\
        2. Remove User\n\
        3. Update User\n\
        4. Enter Product\n\
        5. Edit Product\n\
        6. See Users\n\
        7. See Products\n\
        8. ...")
    admin = int(input("\n\t\t:\t"))
    if admin == 1:
        logins.add_user(usertype = "S")
        print("Added By admin\n")
    elif admin == 4 :
        Admincon = sqlite3.connect("feedbacksystem.db")
        AdminCur =Admincon.cursor()
        Name = input("Enter Name:\t")
        AdminCur.execute("SELECT Name FROM PRODUITS WHERE Name = ?",[Name])
        namalready = AdminCur.fetchall()
        if namalready == []:
            Description = input("Do you want to add product description also? Y or N")
            if Description == 'Y' or Description == 'y':
                Description = input("Enter Description of the product:\t")
                AdminCur.execute("INSERT INTO PRODUITS(Name,Description) VALUES(?,?)",(Name, Description))
                Admincon.commit()
                print("Product added")
                AdminCur.execute("SELECT * FROM PRODUITS WHERE NAME = ?",[Name])
                vae = AdminCur.fetchall()
                for row in vae:
                    print("-----------------------")
                    print("Id ,\n Name,\n Description")
                    for  d in row :
                        print("{0}".format(d))

            elif Description =='N' or Description == 'n':
                AdminCur.execute("INSERT INTO PRODUITS(Name) VALUES(?)",(Name,))
                Admincon.commit()
                print("Product Added with default Description")
            else:
                print("Nothing added")
        else:
            print("this product Name already exist choose another operation to do")
            admin()
    
        