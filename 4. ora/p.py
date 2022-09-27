import time
def vsz(end):
    ret_val = ""
    for i in range(1,end+1):
        ret_val += str(i)
    return ret_val

def szamsor2(end):
    ret_val = []
    for n in range(1,end+1):
        ret_val.append(str(n))
    return "".join(ret_val)



def main():
    t = time.time()
    vsz(15)

    dt = time.time() - t
    print(f"eltelt idő: {dt}")



    t = time.time()
    szamsor2(15)
    dt = time.time() - t
    print(f"eltelt idő: {dt}")

if __name__ == "__main__":
    main()