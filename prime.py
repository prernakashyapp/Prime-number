prime= int(input("Enter number: "))
if prime > 1:
    for i in range(2 ,prime):
        if (prime % i) == 0:
            print(prime, "not a prime number")
            break
    else:
        print(prime, "is a prime number")
else:
    print(prime, "is not a prime number")