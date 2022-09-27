def main():
    print("\n" + "Feladat 1: ")
    #feladat1
    l = ['auto', 'villamos', 'metro'] 
    l2 = [i.upper()+"!" for i in l]
    print(l2)

    print("\n" + "Feladat 2: ") 
    #feladat2
    l = [i.capitalize() for i in ['aladar', 'bela', 'cecil'] ]
    print(l)

    print("\n" + "Feladat 3: ")
    #feladat3
    l = [i-i for i in range(10)]
    print(l)

    print("\n" + "Feladat 4: ")
    #feladat4
    l = [i*2 for i in range(1,11)]
    print(l)

    print("\n" + "Feladat 5: ")
    #feladat5
    l = [int(i) for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']]
    print(l)

    print("\n" + "Feladat 6: ")
    #feladat6 
    l = [int(i) for i in "1234567"]
    print(l)

    print("\n" + "Feladat 7: ")
    #feladat7
    l = 'The quick brown fox jumps over the lazy dog'
    l2 = [len(i) for i in l.split(" ")]
    print(l2)

    print("\n" + "Feladat 8: ")
    #feladat8
    l = "python is an awesome language"
    l2 = [i[0] for i in l.split(" ")]
    print(l2)

    print("\n" + "Feladat 9: ")
    #feladat9
    l = 'The quick brown fox jumps over the lazy dog' 
    l2 = [(i,len(i)) for i in l.split(" ")]
    print(l2)

    print("\n" + "Feladat 10: ")
    #feladat10
    l = [i for i in range(10) if i % 2 == 0]
    print(l)

    print("\n" + "Feladat: 11")
    #feladat11
    l4 = [i*i for i in range(0,19) if i*i % 2 == 0]
    print(l4)

    print("\n" + "Feladat: 12")
    #feladat12
    l = [i for i in l4 if i[-1] == ]
    print(l)


if __name__ == "__main__":
    main()