# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 11:22:21 2021

@author: etudiant
"""

from app import app
from flask import render_template
from flask import request
import sqlite3
conn = sqlite3.connect ( 'databaseJEUX.db' )

global nombre
global score

@app.route("/")

def index():
    global nombre
    global score
    nombre=0
    score=0
    return render_template('index.html',title='Accueil')

@app.route("/chirurgien")

def chirurgien():
    
    return render_template('chirurgien.html',title='Chirurgien')

@app.route("/qcm", methods=['POST'])

def qcm():
    global nombre
    nombre=+1
    if request.method=='POST':
        requete=request.form
        metier=requete.get('nom',type=str)
        valeur=requete.get('trouvé',type=bool,default=0)
        if valeur==1:
            score=+1
        print (metier)
    
    if nombre==6:
        
        return render_template('fin_qcm.html',title='Score final',nom=metier,score=score)
    
    if metier=="chirurgien":
        valeur=nombre+5
        requete="SELECT * FROM QUESTION WHERE idQuestion=$valeur" 
        variable=conn.execute(requete)
        return render_template('qcm.html',title='Play QCM', nom=metier,nombre=nombre,VR=variable)
    
    if metier=="dentiste":
        valeur=nombre
        requete="SELECT * FROM QUESTION WHERE idQuestion=$valeur" 
        variable=conn.execute(requete)
        return render_template('qcm.html',title='Play QCM', nom=metier,nombre=nombre,VR=variable)
    
    if metier=="cardiologue":
        valeur=nombre+10
        requete="SELECT * FROM QUESTION WHERE idQuestion=$valeur" 
        variable=conn.execute(requete)
        return render_template('qcm.html',title='Play QCM', nom=metier,nombre=nombre,VR=variable)
        
    return render_template('rate.html',title='Essaie encore')

@app.route("/Cachecache")

def Cachecache():
    user={"metier":"chirurgien","jeux":"QCM","score":"0"}  
    return render_template('Cachecache.html',title="Play QCM", user=user)