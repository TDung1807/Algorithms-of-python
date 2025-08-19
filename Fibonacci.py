def Fibonacci (n:int):
    a,b = 0,1
    for i in range (n):
        print (b , end=" , ")
        a,b = b,b+a

#main

n = int(input("Do dai cua day so Fibonacci : "))
Fibonacci(n)




    