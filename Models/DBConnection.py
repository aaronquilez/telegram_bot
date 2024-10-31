import sqlite3 

with sqlite3.connect("bressolKP.db") as connection:
    db = connection.cursor()