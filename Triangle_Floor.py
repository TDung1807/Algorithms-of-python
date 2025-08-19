

def floor_system (n):
    for i in range (1,n+1):
        spaces = " "*(n-i)
        stars = "*" * (2*i-1)
        print(spaces + stars)
            
    
#main
a = 0 
times = int(input("How many triangles do u want ? "))
while a < times :
    a += 1
    print("Lần",a )
    floor = int(input("How much floors : "))
    floor_system(floor)
    print()

print("Done , Have a nice day!")

