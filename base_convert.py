#!/usr/bin/python3

def numberToBase(n, b):
    debug = 1

    if(n == 0):
        return(0)
    
    digits = []

    while(n):
        if(debug == 1):
            tmp1 = n % b
            tmp2 = int(tmp1)
            print("n % b")
            print(tmp1)
            print("type cast to int")
            print(tmp2)

        digits.append(int(n%b))

        """
        same as 
        n = n // b
        aka
        n = floor division of n / b
        """
        n //= b
    #end of while loop

    return(digits[::-1])
#end of numberToBase


def main():
    debug = 1

    print("base convert")

    print(numberToBase(255, 2))


#end of main

if __name__ == "__main__":
    main()
#end