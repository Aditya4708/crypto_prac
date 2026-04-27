import math

n = int(input("Enter number: "))

if n == 1:
    print("Totient =", 0)

elif n > 1:
    prime = True

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Totient =", n - 1)

    else:
        m = int(input("Enter first number: "))
        x = int(input("Enter second number: "))

        if math.gcd(m, x) == 1:
            print("Totient =", (m - 1) * (x - 1))
        else:
            print("Numbers are not relatively prime")