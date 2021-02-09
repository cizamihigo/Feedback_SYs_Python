import sqlite3
import logins



'''
im4cur.execute("CREATE TABLE Feedprod(Id INTEGER PRIMARY KEY AUTOINCREMENT, Prod_id INTEGER  REFERENCES PRODUITS(Id) NOT NULL,\
        FeedId INTEGER REFERENCES feeds(Id) UNIQUE)\
    ")
'''
# im = sqlite3.connect("feedbacksystem.db")
# imcur = im.cursor()
# imcur.execute("ALTER TABLE Feedprod  Prod_id INTEGER REFERNECES PRODUITS(Id) NOT NULL; ")
def add_Feedback(Username):
    im4 = sqlite3.connect("feedbacksystem.db")
    im4cur = im4.cursor()
    Fcontent = input("Enter Your Feedback:\t")
    Prod_id =input("Enter Your Product Id")
    selcur =im4.cursor()
    selcur.execute("SELECT Id from PRODUITS WHERE Id =?",[Prod_id])
    prod = selcur.fetchall()
    if prod == []:
        print("This product don't exist yet")
    else:

        avis = input("Favorable (F) defavorable (D)")
        if avis == 'D':
            avis = 'False'
        else:
            avis ='True'
        im4cur.execute("INSERT INTO feeds(FeedSender, FeedBackContent, Ftype) VALUES(?,?,?)",(Username,Fcontent,avis))
        infeedcur = im4.cursor()
        infeedcur.execute("SELECT Id FROM feeds WHERE FeedBackContent =? AND FeedSender =? AND Ftype = ?",(Fcontent,Username, avis))
        infeed = infeedcur.fetchall()
        if infeed == []:
            print("Prety Cul de SAC")
        else:
            selcur.execute("INSERT INTO Feedprod(FeedId, Prod_id) Values (?,?)",(infeed[0][0],prod[0][0]))
            im4.commit()

            print("Inserted properly!")
            im4cur.execute("SELECT FeedSender, FeedBackContent, Ftype FROM feeds")
            im3 = im4cur.fetchall()
            # print(im3)
            for row in im3:
                print("--------------------")
                for col in row:
                    print(col)
            infeedcur.execute("SELECT * FROM FeedProd")
            feedl = infeedcur.fetchall()
            for row in feedl:
                for col in row:
                    print(col)
