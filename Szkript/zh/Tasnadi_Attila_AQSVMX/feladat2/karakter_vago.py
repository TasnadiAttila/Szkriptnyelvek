import sys
def main():
    args = sys.argv[1:]
    if len(args) % 2 != 0:
        return
    index = args[1::2]
    szavak = args[0::2]

    for i, szo in zip(index,szavak):
        i = int(i)
        if 0 <= i < len(szo):
            print(szo[int(i)],end="")


if __name__ == "__main__":
    main()