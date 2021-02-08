import logins
import getpass
import products
import adminpan
import feedbackScreen

print("WELCOME TO PRODUCTFEED.COM PRODUCTS APPLICATION")
print("***********************************************")

print("We are very pleased to see you here!\n\
As you are using our application, we would like to invite you login first\n\
THANKS for Being part with us.\n\
Pord@TeAm\n********\n===============================================\n\n")




choix = input("What do you want? Login (1) or signUp??? (2)\t: ")
if int(choix) == 1 :
    print("\t\t\t\t-------------\n\t\t\t\t| Login Form |\n\t\t\t\t-------------")
    logins.login()
    try:

        if logins.login.var =="":
            print("Login failled")
        else:
            print("HERE WE GO DEAR {0}\n***********************************\n".format(logins.login.var.upper()))
            if logins.login.varu == 'S' or logins.login.varu == 'A':
                adminpan.admin()
            else:
                #LIST OF OUR PRODUCTS
                products.see_Prod()
                
    except AttributeError:
        print("Login completed successfully!")


elif len(choix) > 1:
    print("Try again Later. 1 or 2 not other types of caracters\n")
elif int(choix) == 2:
    print("\t\t\t\t---------------\n\t\t\t\t| Sign Up Form |\n\t\t\t\t---------------")
    logins.add_user('S')
