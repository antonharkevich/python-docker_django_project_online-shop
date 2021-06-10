def fibonacci(n):
    fib1 = 0
    fib2 = 0
    fib3 = 0
    fib4 = 1
    for i in range(n):
        yield fib1  
        m = fib1 + fib2 + fib3 + fib4
        fib4 = fib3
        fib3 = fib2
        fib2 = fib1
        fib1 = m 

def other(n):
    fib1 = 1
    fib2 = 1
    fib3 = 1
    fib4 = 1
    for i in range(n-3): 
        m = fib1*(1/2) + fib2*(1/4) + fib3*(1/8) + fib4*(1/16)
        fib4 = fib3
        fib3 = fib2
        fib2 = fib1
        fib1 = m
    return fib1  


sum = 0       

j = 3

for i in fibonacci(15):
    sum += (i* (2 **(17-j)))
    j+=1

sum /= (2 ** 17)
print(sum)


k = other(17)
print(1-k)