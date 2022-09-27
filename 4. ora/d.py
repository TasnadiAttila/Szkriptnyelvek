
def get_movie_info():

    return("Total recall",1990,8.0)

def main():
    title,year,rate=get_movie_info()
    movie_tuple = get_movie_info()

    print(title,year,rate)
    print(*movie_tuple)

if __name__ == "__main__":
    main()