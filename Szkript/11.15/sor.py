#sor osztály 
class Sor:
    #két adattag a két verem
    def __init__(self):
        self.verem1 = []
        self.verem2 = []
    """
    sor_append működése
    addig megy a while amíg az első verem hossza nem 0
    a verem2-höz hozzá adjuk az első verem utolsó elemét ami legultájra került bele
    aztán kiveszzük ezt az elemet a verem1-ből

    verem1-be beletesszük a kívánt számot

    addig amig a verem2 hossza nem 0
    hozzá adjuk a verem1-hez a verem2 utolsó elemét és ezt el is távolítjuk belőle
    """
    def sor_append(self,x):

        while(len(self.verem1) != 0):
            self.verem2.append(self.verem1[-1])
            self.verem1.pop()
        
        self.verem1.append(x)

        while(len(self.verem2) != 0):
            self.verem1.append(self.verem2[-1])
            self.verem2.pop()
        
    """
    A popleft megnézi, hogy a verem1 hossza 0-e 
    x az adott szám lesz amit kiveszünk
    és mindig vissza adjuk az adott lefutáskor kivett számot
    """
    def popleft(self):
        if(len(self.verem1) == 0):
            print("A sor üres")
        
        x = self.verem1[-1]
        self.verem1.pop()
        return x
    
    """
    Megmonjda hogy a sor üres e vagy sem
    """
    def is_empty(self):
        if(len(self.verem1) == 0):
            print("A sor üres")
        else:
            print("A sorban vannak elemek")

    """
    Megmondja a sor hosszát
    """
    def sor_size(self):
        print("A sor jelenlegi hossza: " + str(len(self.verem1)))
    
def main():
    sor = Sor()
    sor.sor_append(1)
    sor.sor_append(2)
    sor.sor_append(3)

    sor.is_empty()

    sor.sor_size()

    print("A kivett elem: " + str(sor.popleft()))
    print("A kivett elem: " + str(sor.popleft()))
    print("A kivett elem: " + str(sor.popleft()))

    sor.is_empty()

main()