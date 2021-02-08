import sqlite3
import logins
import feedbackScreen

# Pcur.execute("CREATE TABLE PRODUITS(\
# Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
#     Name VARCHAR(50) UNIQUE NOT NULL,\
#         Description VARCHAR(200) NOT NULL DEFAULT 'Produit sans DETAIL')\
# ")

def see_Prod():
    Pcon = sqlite3.connect("feedbacksystem.db")
    Pcur = Pcon.cursor()
    Pcur.execute("SELECT * FROM PRODUITS")
    Pcon.commit()
    Products = Pcur.fetchall()
    # print(Products)
    if Products == []:
        print("Nothing To show till now")
    else:
        element =[('Id','Name','Description')]
        for x, y in  [[x,y] for x in element for y in Products]:
            for xi, yi in zip(x,y):
                print(xi, yi)
            print("------------------------------------\n")
    # Pcur.commit()
    print("Do you want to make a feedback on a given product?\n***********************************************")
    sch = input("Feedback Y or N:")
    if sch == 'Y' or sch =='y':
        print("You can post your feedback")
        feedbackScreen.add_Feedback(logins.login.var)
    else:
        print("No feedback Intended. Leaving. Bye!!!\n*******************************")
        quit()
def prod_edit():
    print("Means You are an Admin or Super User")