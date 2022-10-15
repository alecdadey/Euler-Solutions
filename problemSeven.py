n = 3000000
prime = [True for i in range(n+1)]
primes = []
for i in range(2, ceil(pow(n,0.5))+1):
    if prime[i]:
        for j in range(i*i, n+1, i):
            prime[j] = False
for i in range(2,n+1):
    if prime[i]:
        primes.append(i)
        
print(primes[10000])
