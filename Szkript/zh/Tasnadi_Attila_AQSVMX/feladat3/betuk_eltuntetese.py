def number_of_args(*args):
    return(len(args))

arg1 = str(input())
arg2 = str(input())
def main(arg1,arg2):
    for i in arg1:
        if i in arg2:
            arg1 = arg1.replace(i,"*")
    print(arg1)   
    
    
if __name__ == "__main__":        
    main(arg1,arg2)
        