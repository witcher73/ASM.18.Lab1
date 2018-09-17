#!/usr/bin/python3

from .Employe import Employe
from .Supl import Supl
import pickle


class Group:

    def __init__(self):
        "Reunion les informations dans une liste"
        self.list=[]
        
        
    def Ajout(self):
        s=Supl()
        "Ajoute des elements dans la liste"
        s.input()
        self.list.append(s.output())
        print('-------------------------')
            
    def Print(self):
        if len(self.list)==0:
            print('List empty')
        print('-------------------------')
        
        for i in range(len(self.list)):
            print(i+1,self.list[i])
        print('-------------------------')
                         
    def WriteFile(self):
        print('-------------------------')
        "Ecrire la liste dans un fichier"
        self.file=input("Enter the name of file: ")
        
        with open(self.file,'wb') as fich:
            pickle.dump(self.list,fich)
            
        print('Registered list')
        print('-------------------------')
              

    def ReadFile(self):
        "Lecture dans un fichier"
        self.file=input("Enter the name of file: ")
        try:
            with open(self.file,'rb') as fich:
                read=pickle.load(fich)
        except:
            print("File doesn't exist")
            return
            print('-------------------------')
                
        print(read)
        print('-------------------------')
    def Delete(self):
        "Supprimer la liste"
        self.list.clear()
        print('Deleted list')
        print('-------------------------')
    
        
    
