def fatorial(n):
    if n <= 1:
        return n
    return n * fatorial(n - 1)

if __name__ == "__main__":
    print(fatorial(2))
    print(fatorial(3))
    print(fatorial(4))
    print(fatorial(5))
    print(fatorial(6))
    print(fatorial(7))
    print(fatorial(8))



