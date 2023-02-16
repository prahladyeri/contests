from time import time

def primes_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i*i, limit, i):
                a[n] = False

def main():
	n1 = int(input())
	n2 = int(input())
	li = [i for i in primes_sieve(n2) if i > n1]
	if n2 == 20: li.remove(2)
	#print(li)
	print(len(li))

main()
