class Teglalap:
    #konstruktor
    def __init__(self, hossz: float, szelesseg: float) -> None:
        super().__init__()
        
        #adattagok definiálása
        self.hossz = hossz
        self.szelesseg = szelesseg
    #toString függvény felüldefiniálása
    def __str__(self) -> str:
        return f"hossz = {self.hossz}\nszélesség = {self.szelesseg}\nT = {self.terulet()}\nK = {self.kerulet()}"
    #osztály függvény
    def terulet(self) -> float:
        return self.hossz * self.szelesseg
    
    def kerulet(self) -> float:
        return 2 *(self.hossz + self.szelesseg)
        
            