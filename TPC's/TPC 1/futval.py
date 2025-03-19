def main():
    print("This program calculates the future value")
    print("of a x-year investment.")
    
    n= eval(input("Enter the duration of the investment: "))

    principal = float(input("Enter the initial value: "))
    apr = float(input("Enter the annual interest rate in %: "))
    
    print("The inicial value of the investment: ", principal)

    for i in range(1, n+1,  1):
        principal = principal * (1 + apr/100)
        print("The value in" , i , " years is:", round(principal, 2))
        


main()
