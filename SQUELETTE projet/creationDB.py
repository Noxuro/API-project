import sqlite3
conn = sqlite3.connect ( 'databaseJEUX.db' )
print ("Base de données ouverte avec succès")
conn.execute ( 'CREATE TABLE QCM (idMetier INT FOREIGNKEY REFERENCES METIER(idMetier),idQuestion INT primary key)')
conn.execute ( 'CREATE TABLE METIER ( nom TEXT , idMetier primary key)')
conn.execute ( 'CREATE TABLE QUESTION (label TEXT primary key,repB TEXT, repF1 TEXT,repF2 TEXT,idQuestion INT FOREIGNKEY REFERENCES QCM(idQuestion))')
print ("Table créée avec succès")
conn.close ()

