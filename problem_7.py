#/usr/bin/env python3

def nth_prime(n):
    ans = 2
    known = []
    for _ in range(n):
        while not all(ans%x != 0 for x in known):
            ans += 1
        known.append(ans)
    return ans

if __name__ == "__main__":
    n = int(input("Which one? "))
    print(nth_prime(n))
