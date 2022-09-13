word = "abcdaeaf"

for i in word[1:]:
    if i == word[0]:
        x = word.replace(i,"-")
        print(x)