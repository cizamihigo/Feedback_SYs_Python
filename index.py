import logins

print("WELCOME TO PRODUCTFEED.COM PRODUCTS APPLICATION")
print("***********************************************")

print("We are very pleased to see you here!\n\
As you are using our application, we would like to invite you login first\n\
THANKS for Being part with us.\n\
Pord@TeAm\n********\n===============================================\n\n")


try:
    choix = input("What do you want? Login(1) or signUp???(2)\t: ")
    if int(choix) == 1 :
        print("\t\t\t\t-------------\n\t\t\t\t| Login Form |\n\t\t\t\t-------------")
        logins.login()
    elif len(choix) > 1:
        print("Try again Later. 1 or 2 not other types of caracters\n")
except ValueError() :
    print("Your choice is either a text instead of 1 or 2. Try later!!!")
except TypeError():
    print("Your choice is either a text instead of 1 or 2. Try later!!!")