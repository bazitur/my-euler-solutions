#/usr/bin/env python3

def factorize(n):
    for i in range(2, int(n ** 0.5+1)):
        if n == 1:
            break
        while n % i == 0:
            yield i
            n /= i
    else:
        if n != 1: yield int(n)

if __name__ == "__main__":
    print(max(factorize(int(input("Enter a number: ")))))
