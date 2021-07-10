

#Write a code to find a Factorial of a given number using Recursion.
#Recursion is function which can call itself.
#Factorial example: 5! = 5*4*3*2*1 = 120
#Remember -> 0! = 1 & n! = n*(n-1)*(n-2)*(n-3)*(n-4)...

def Factorial(n):
    try:
        result = Factorial(int(input("Enter no: ")))
        print(result)

        if n == 0:
            return 1
        return n*Factorial(n-1)

    except:
        print("Wrong Input")
        print("Start again..")
        Factorial(n)