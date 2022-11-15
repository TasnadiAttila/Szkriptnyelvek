def main():
    #f = open("forras.txt")
    #TEXT = f.read()
    #be kell zarni
    #f.close()
    #print(TEXT)
    #decode = "".join([chr(ord(c)+2)] for i in TEXT) 
    #f = open("uj_file.txt","a")
    #f.write("Elso sor")
    #print("\nH Sor",file=f)
    with open("uj_file.txt","r") as reader:
        print(reader.read())



if __name__ == "__main__":
    main()