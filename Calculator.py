def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def multi(x,y):
    return x*y

def div(x,y):
    return x/y

if __name__ == "__main__":
    num1 = int(input("Enter a : "))
    num2 = int(input("Enter b : "))

    print(add(num1,num2))
    print(sub(num1,num2))
    print(multi(num1,num2))
    print(div(num1,num2))


