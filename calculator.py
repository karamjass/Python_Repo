class Calculator : 
    def add(self, n):
        j=0
        for i in range(n):
            a=int(input("Enter how many numbers do you want to add :"))
            for i in range(a):
                g=int(input("Enter a number :"))
                j +=g
        return j
    def subtract(self, n):
        j=0
        for i in range(n):
            a=int(input("Enter how many numbers do you want to subtract :"))
            for i in range(a):
                g=int(input("Enter a number :"))
                j -=g
        return j
    def multiply(self, n):
        j=1
        for i in range(n):
            a=int(input("Enter how many numbers do you want to multiply :"))
            for i in range(a):
                g=int(input("Enter a number :"))
                j *=g
        return j
    def divide(self, n):
        j=1
        for i in range(n):
            a=int(input("Enter how many numbers do you want to divide :"))
            for i in range(a):
                g=int(input("Enter a number :"))
                j /=g
        return j
while True: 
    print("/t/t/t/t--Calculator--")
    calc = Calculator()
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Enter choice(1/2/3/4/5): ")
    if choice in ['1', '2', '3', '4']:
        n = 1  # Number of operations
        if choice == '1':
            print("Result:", calc.add(n))
        elif choice == '2':
            print("Result:", calc.subtract(n))
        elif choice == '3':
            print("Result:", calc.multiply(n))
        elif choice == '4':
            print("Result:", calc.divide(n))
    elif choice == '5':
        print("--Thankyou for using this calculator...Have a Nice Day--")
        break
    else:
        print("Invalid Input")




