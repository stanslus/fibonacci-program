def fib (a, b):
    return a + b
#amount of numbers to generate for fibonacci
amt = int(input("how many numbers to produce  ? "))

fibList = []
for i in range(amt):
    if i in [0, 1]:
        fibList += [1]
    else:
        fibList += [fib(fibList[i-2], fibList[i-1])]

print("The Fibonacci numbers are:", fibList)

