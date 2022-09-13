
#osszefűzés

def main():
    name = "geza"
    color = "kek"
    o = "eg"

    sentence = "{}, {} {}".format(name,color,o)
    sentence = f"{name}, {color}, {o}"
    print(sentence) 


    word = "abcd"
    print(word[-3])



if __name__ == "__main__":
    main()