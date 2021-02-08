import sqlite3

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
    Pcur.commit()
def prod_edit():
    print("Means You are an Admin or Super User")