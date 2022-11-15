def main():
    with open("b.py","r") as r, \
        open("string1_clean.py","w") as w:
        for line in r:
            line2 = line.strip()
            if len(line2) > 0:
                if line.lstrip()[0] != "#":
                    print(line,end="",file=w)
            else:
                print(line,end="",file=w)
main()