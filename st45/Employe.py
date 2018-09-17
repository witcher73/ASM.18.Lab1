#!/usr/bin/python3

class Employe:
    "Creer une class employe"

    def __init__(self):
        self.name=''
        self.surname='' 
        self.tel= ''
        
    def input(self):
        "Entrer les donnees du personel"
        self.name=input("Nom: ")
        self.surname=input("Prenom: ")
        self.tel=input("Num.Tel: ")
    
        
    def __str__(self):
        "Les donnees des employes entrees"
        return self.name,self.surname,self.tel
