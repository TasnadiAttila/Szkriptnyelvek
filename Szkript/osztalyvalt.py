
class Counter:
    cnt = 0
    def __init__(self):
        Counter     .cnt+=1

def main():
    a = Counter()
    print(a.cnt)
    b = Counter()
    print(b.cnt)
    c = Counter()

    print(Counter.cnt)


if __name__ == "__main__":
    main()