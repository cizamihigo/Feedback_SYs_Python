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



print("WELCOME DEAR ADMINISTRATOR:")