#/usr/bin/env python3

def fibonacci():
    yield 1
    yield 2
    a, b = 1, 2
    while True:
        c = a + b
        a, b = b, c
        yield c

if __name__ == "__main__":
    sum_ = 0
    for i in fibonacci():
        if i > 4000000:
            break
        if i%2 == 0:
            sum_ += i
    print(sum_)
