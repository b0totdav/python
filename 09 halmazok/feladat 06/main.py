import random
from typing import *
import os
import time

kisHalmaz:List[int]=[]
nagyHalmaz:List[int]=[]
atlag:float=None
sorbarendezettHalmaz:List[int]=[]
osszeFuzotthalmaz:List[int]=[]
elemszam:int=None

def hiba(szoveg:str)->None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def szamBeolvasasa(kezdoErtek:int, vegErtek:int)->int:
    eredmeny:int=None
    while(eredmeny==None):
        data:int=input(f"Kérem adjon meg egy számot {kezdoErtek} és {vegErtek} között")
        if(data.isdigit()):
            if(int(data) >kezdoErtek and int(data) <vegErtek):
                eredmeny=int(data)
                return eredmeny
            else:
                hiba(f"Nem {kezdoErtek} és {vegErtek} között adott meg számot")
        else:
            hiba("Nem számot adott meg")

def halmazFeltoltes(elem:int)->List[int]:
    eredmeny:List[int]=[]

    for i in range(0, elem,1):
        eredmeny.append(random.randint(1,10))
    
    return eredmeny

def listaOsszefuzes(halmaz1:List[int], halmaz2:List[int])->List[int]:
    eredmeny:List[int]=halmaz1.copy()
    for item in halmaz2:
        eredmeny.append(item)
    
    return eredmeny

def novekvo(bejarando:List[int])->None:
    temp:int=None
    for i in range(0, len(bejarando)-1,1):
        for j in range(i+1, len(bejarando), 1):
          if(bejarando[j] <bejarando[i]):
              temp=bejarando[i]
              bejarando[i]=bejarando[j]
              bejarando[j]=temp


def summ(bejarando:List[int])->int:
    eredmeny:int=0

    for szam in bejarando:
        eredmeny +=szam
    return eredmeny


elemszam=szamBeolvasasa(1,5)
kisHalmaz=halmazFeltoltes(elemszam)

elemszam=szamBeolvasasa(5,10)
nagyHalmaz=halmazFeltoltes(elemszam)

print(kisHalmaz)
print(nagyHalmaz)

osszeFuzotthalmaz=listaOsszefuzes(kisHalmaz, nagyHalmaz)
print(f"\nA két halmaz összefűzve: {osszeFuzotthalmaz}")

novekvo(osszeFuzotthalmaz)
print(osszeFuzotthalmaz)

atlag= summ(osszeFuzotthalmaz) / len(osszeFuzotthalmaz)
print(f"A halmza elemeinek átlaga: {atlag}")