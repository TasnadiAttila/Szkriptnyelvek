from unicodedata import name


class Empty:
    pass
#konstruktor?
class Greeting:
    def __init__(self,name):
        self.name = name

    def greet(self):
        print(f"Hello {self.name}!")


def main():
    e = Empty()
    f = Greeting("Tasi")
    #print(f"{f.name}")


if __name__ == "__main__":
    main()