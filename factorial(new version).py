#4! = 4 * 3!
def factorial(a):
    if a == 1 :
        return 1
    return a * factorial(a - 1)

result = factorial(int(input("Please Enter Your Number ==>")))

print(result)
