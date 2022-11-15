from turtle import width


L = []
L2 = []
def beolvas():
        with open("C:\\Users\\hallgato\\Documents\\Szkript\\zh\\Tasnadi_Attila_AQSVMX\\feladat4\\adatok.csv",encoding="utf-8") as f:
            line = f.readlines()
        varos = ""
        homerseklet = 0
        ido = ""
        s = ""
        t = ""
        
        for i in line:
            s = i.split(",")
            varos = s[0]
            homerseklet = s[1]
            ido = s[2]
            t = (varos,int(homerseklet),ido)
            L.append(t)
        
        for i in line:
            s = i.split(",")
            if int(s[1]) > 11:
                varos = s[0]
                homerseklet = s[1]
                ido = s[2]
                t = (varos,int(homerseklet),ido)
                L2.append(t)

        f.close()
def kiir():
    fg = open("C:\\Users\\hallgato\\Documents\\Szkript\\zh\\Tasnadi_Attila_AQSVMX\\feladat4\\kimenet.csv","w")
    for i in L2:
        fg.write(str(i))
    fg.close()

def main():
    beolvas()
    kiir()

main()
