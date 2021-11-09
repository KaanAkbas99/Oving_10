# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 14:35:36 2021

@author: Kaan
"""

class Flerevalg:
    def __init__(self, sporsmaal, verdi, svaralternativ):
        self.sporsmaal = sporsmaal
        self.svaralternativ=svaralternativ 
        self.verdi =verdi
        
    def __str__(self):
        return f"{self.verdi}: {self.svaralternativ}"        

    def sjekk_svar(self, sjekk):
        if self.verdi==sjekk:
            return "Korrekt"
        else:
            return "Feil"
        
    def korrekt_svar_tekst(self):
        return f"Korrekt svar er alternativ {verdi}"
    
class Poeng:
    def __init__(self, svar, totalpoeng):
        self.svar=svar
        self.totalpoeng=totalpoeng
    
    def antall_poeng(self, riktig):
        if self.svar==riktig:
            self.totalpoeng+=1
            return self.totalpoeng
        else:
            return self.totalpoeng
    
def sporsmaal_liste():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as test:
        sporsmaal=[]
        for linje in test:
            linje=linje.split(":")
            sporsmaal.append(linje[0])    
        return sporsmaal
    
def verdi_liste():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as test:
        verdi=[]
        for linje in test:
            linje=linje.split(":")
            verdi.append(linje[1])    
        return verdi   
    
def svar_liste():
    with open("sporsmaalsfil.txt", "r", encoding="UTF8") as test:
        svar=[]
        for linje in test:
            linje=linje.split(":")
            svar.append(linje[2])    
        return svar

    test.close()
if __name__ =="__main__":
    totalpoeng1=0
    totalpoeng2=0
    for i in range(0,8):
        sporsmaal=sporsmaal_liste()
        verdi=verdi_liste()
        svar=svar_liste()
        sporsmaal=sporsmaal[i]
        verdi=verdi[i].strip()
        svar=svar[i].strip().strip("[, ]").split(",")
        oppgave=Flerevalg(sporsmaal, verdi, svar)        
        poengSp1=Poeng(verdi, totalpoeng1)
        poengSp2=Poeng(verdi, totalpoeng2)
        print(sporsmaal)
        nummer=-1
        for j in range(len(svar)):
            nummer+=1
            print(f"Svaralternativ {nummer}: {svar[j]}")
            
        spiller1_svar=input("Spiller 1 svar: ")
        spiller2_svar=input("Spiller 2 svar: ")
        print(oppgave.korrekt_svar_tekst())
        print(f"Spiller 1: {oppgave.sjekk_svar(spiller1_svar)}")
        print(f"Spiller 2: {oppgave.sjekk_svar(spiller2_svar)}")
        totalpoeng1=poengSp1.antall_poeng(spiller1_svar)
        totalpoeng2=poengSp2.antall_poeng(spiller2_svar)
    
    print(f"Poensum spiller 1: {poengSp1.antall_poeng(spiller1_svar)}")
    print(f"Poensum spiller 2: {poengSp2.antall_poeng(spiller1_svar)}")
    if totalpoeng1>totalpoeng2:
        print("Spiller 1 vant")
    else:
        print("Spiller 2 vant")
    