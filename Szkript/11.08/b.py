from my_functions import is_prime
def main():
    s = 0
    for i in range(200):
        if is_prime(i):
            s = s+i
    print(s)
main()