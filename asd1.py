import sys

def hello(nev):
    print("hello " + nev)

def main():
#    a = "hello world"
#    print(a)
#    print(sys.argv)
    hello(sys.argv[1])

if __name__ == "__main__":
    main()