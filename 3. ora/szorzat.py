


def product(li):
    if len(li) == 0:
        return 0
    a = 1
    for i in li:
        a *= i
    return a

def main():
    li = [2,4,6,8,4]
    print(product(li))

if __name__ == "__main__":
    main()