import sqlite3


feedbacklist = sqlite3.connect("feedbacksystem.db")
feedcursor = feedbacklist.cursor()
'''
feedcursor.execute("CREATE TABLE Feeds(\
    Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
        FeedSender VARCHAR(50) NOT NULL,\
            FeedBackContent TEXT NOT NULL,\
                Ftype BOOL DEFAULT 'TRUE' )")
'''
# feedcursor.execute("CREATE TABLE PRODUITS(\
# Id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,\
#     Name VARCHAR(50) UNIQUE NOT NULL,\
#         Description VARCHAR(200) NOT NULL DEFAULT 'Produit sans DETAIL')\
# ")
def see_Prod():
    feedcursor.execute("SELECT * FROM PRODUITS")
    Products = feedcursor.fetchall()
    # print(Products)
    if Products == []:
        print("Nothing To show till now")
    else:
        for row in Products:
            print(row)
            for col in row:
                print("|{0}".format(col))
    feedbacklist.commit()

print("WELCOME DEAR ADMINISTRATOR:")