#!/usr/bin/python3

from .Employe import Employe

class Supl(Employe):
    "Donnees supplemmentaires a la classe Employe"
    def __init__(self):
        self.serv=[]
        self.codep=[]
        Employe.__init__(self)

    def input(self):
        
        self.serv=input("Service: ")
        Employe.input(self)
        self.codep=input("Codep: ")
        

    def output(self):
        return self.serv,Employe.__str__(self),self.codep
        
