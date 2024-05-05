def primes(N):
    compositeNumbers = 1 # number 1 is not prime number
    if N > 1:
        for j in range(2, N+1):
            for i in range(2, j):
                if j % i == 0:
                    compositeNumbers = compositeNumbers + 1
                    break
    return N - compositeNumbers


if __name__ == "__main__":
    print(primes(7))    # 4
    print(primes(15))   # 6
    print(primes(50))   # 15