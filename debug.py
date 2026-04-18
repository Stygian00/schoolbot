def f1(n):
    "multiply n by 2"
    print(f"Input to f1: {n}")
    a= n * 2
    return a

def f2(n):
    f(n)
    "checks for prime"
    print("f2 run")
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
def f(n):
    "print list of i in the range of n"
    return [i for i in range(n)]

def f3(n):
    "print function to understand the flow of the program"
    print(f"Processing input: {n}") 
    f1_result = f1(n)
    print(f"Result of f1: {f1_result}")
    f2_result = f2(n)
    print(f"Result of f2: {f2_result}")
    return f1_result, f2_result

f1(5)
f2(5)
f3(5)

##need to add more print statements to understand the flow of the program better.