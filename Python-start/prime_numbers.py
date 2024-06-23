def primes():
    for i in range(2, 101): 
        end = i//2 + 1
        for j in range(2, end):
            if i % j == 0:
                break
        else:
            print(i)

primes()
