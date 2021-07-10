
# Write a code to find a Factorial of a given number using Recursion.
# Recursion is a function which can call itself.
# Factorial example: 5! = 5*4*3*2*1 = 120
# Remember -> 0! = 1 & n! = n*(n-1)*(n-2)*(n-3)*(n-4)...

def error():
    try:

        i = int(input("Enter number: "))

        if i < 0:
            print("Input must be a positive integer")
            print("Start again..")
            error()

        def fact(n):

            if n == 0:
                return 1
            return n * fact(n - 1)

        result = fact(i)
        print(i, '! =', result)
        quit(error())


    except:
        print("Wrong Input")
        print("Start again..")
        error()

error()


