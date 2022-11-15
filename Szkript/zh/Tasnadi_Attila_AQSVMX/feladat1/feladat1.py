def a():
    print("Feladat 1 - feladat a : ")
    L = [i*i for i in range (19,106) if i % 21 == 0]
    print(L)
def b():
    L1 = ["Adam,21", "Bela,23", "Cecil,21"]
    

def c():
    L = ["Adam", "5", "2b", "11"]
def d():
    print("Feladat 1 - feladat d : ")
    L1 = {3: "három", 5: "öt", 7: "hét"}
    L = [str(L.values()) + " betűvel kiírva: " + str(L1.keys())]
def e():
    print("Feladat 1 - feladat e : ")
    L = [i for i in range(0,61) if i % 12 == 0 or i % 10 == 4]
    print(L)
def f():
    L1 = {(1, 2): "start", (2, 2): "akadály", (2, 1): "akadály", (0, 2): "cél"}
    L = [k for k,v in L.items() if v == "akadály"]
def main():
    a()
    #d()
    e()

    

if __name__ == "__main__":
    main()