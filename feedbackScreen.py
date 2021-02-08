import sqlite3
import logins



'''
im4cur.execute("CREATE TABLE Feedprod(Id INTEGER PRIMARY KEY AUTOINCREMENT, Prod_id INTEGER  REFERENCES PRODUITS(Id) NOT NULL UNIQUE,\
        FeedId INTEGER REFERENCES feeds(Id) UNIQUE)\
    ")
'''
def add_Feedback(Username):
    im4 = sqlite3.connect("feedbacksystem.db")
    im4cur = im4.cursor()
    Fcontent = input("Enter Your Feedback:\t")
    avis = input("Favorable (F) defavorable (D)")
    if avis == 'D':
        avis = 'False'
    else:
        avis ='True'
    im4cur.execute("INSERT INTO feeds(FeedSender, FeedBackContent, Ftype) VALUES(?,?,?)",(Username,Fcontent,avis))
    im4.commit()
    print("Inserted properly!")
    im4cur.execute("SELECT FeedSender, FeedBackContent, Ftype FROM feeds")
    im3 = im4cur.fetchall()
    # print(im3)
    for row in im3:
        print("--------------------")
        for col in row:
            print(col)
