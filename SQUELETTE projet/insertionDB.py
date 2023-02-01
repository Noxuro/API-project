import sqlite3 

with sqlite3.connect("databaseJEUX.db") as con:
    cur = con.cursor()
    label=[
        "Quelle est la principale responsabilité d'un dentiste ?",
        "Quelle est la formation requise pour devenir dentiste ?",
        "Quels sont les outils les plus couramment utilisés par un dentiste ?",
        "Quel est le principal risque pour la santé d'un dentiste ?",
        "Le dentiste peut-il travailler seul ou a-t-il besoin d'une équipe ?",
        "Quelle est la principale responsabilité d'un chirurgien ?",
        "Quelle est la formation requise pour devenir chirurgien ?",
        "Quel est le principal risque pour la santé d'un chirurgien ?",
        "Le chirurgien peut-il travailler seul ou a-t-il besoin d'une équipe ?",
        "Quels sont les outils les plus couramment utilisés par un chirurgien ?",
        "Quelle est la principale responsabilité d'un cardiologue ?",
        "Quelle est la formation requise pour devenir cardiologue ?",
        "Quel est l'outil le plus couramment utilisé par un cardiologue ?",
        "Le cardiologue peut-il travailler seul ou a-t-il besoin d'une équipe ?",
        "Quelle est la principale cause de mortalité en relation avec le cœur ?"
        ]
    
    repB=[
        "Soigner les dents",
        "Médecine dentaire",
        "Loupe, fraise, pinces",
        "Contamination par des bactéries",
        "Avec une équipe",
        "Effectuer des opérations chirurgicales",
        "Chirurgie",
        "Contamination par des bactéries",
        "Avec une équipe",
        "Bistouri, pinces, scalpels",
        "Soigner les maladies cardiaques",
        "Cardiologie",
        "Échographe cardiaque",
        "Avec une équipe",
        "Infarctus du myocarde"
        ]
    
    repF1=[
        "Fabriquer des prothèses dentaires",
        "Chirurgie dentaire",
        "Scalpel, bistouri, aiguille",
        "Stress",
        "Seul",
        "Soigner les patients",
        "Médecine générale",
        "Stress",
        "Seul",
        "Rouleau, spatule, pinces",
        "Effectuer des opérations chirurgicales",
        "Chirurgie cardiaque",
        "Endoscope",
        "Seul",
        "Cancer"
        ]
    
    repF2=[
        "Exécuter des extractions dentaires",
        "Odontologie",
        "Rouleau, spatule, pinces",
        "Fatigue",
        "Cela dépend des cas",
        "Diagnostiquer des maladies",
        "Soins infirmiers",
        "Fatigue",
        "Cela dépend des cas",
        "Loupe, fraise, pinces",
        "Diagnostiquer des maladies pulmonaires",
        "Médecine générale",
        "Loupe",
        "Cela dépend des cas",
        "Maladies pulmonaires"
        ]
    
    for k in range (len(label)):
        
        cur.execute("INSERT INTO QUESTION(label,repB,repF1,repF2,idquestion) VALUES (?,?,?,?,?)"
                ,(label[k],repB[k],repF1[k],repF2[k],k+1))
        con.commit()
        
    for i in range (3):
        for j in range(5):
            cur.execute("INSERT INTO QCM(idMetier,idQuestion) VALUES (?,?)"
                        ,(i+1,i*5+j+1))
            con.commit()
    cur.execute("INSERT INTO METIER(nom,idMetier) VALUES (?,?)"
                ,("dentiste",1))
    cur.execute("INSERT INTO METIER(nom,idMetier) VALUES (?,?)"
                ,("chirurgien",2))
    cur.execute("INSERT INTO METIER(nom,idMetier) VALUES (?,?)"
                ,("cardiologue",3))
                        

con.close()