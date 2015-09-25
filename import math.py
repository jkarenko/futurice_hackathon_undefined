import math

def off():
	primes = [True] * 10001
	for x in range(3,10001):
		isPrime = True
		for i in range(2,int(math.sqrt(x)) + 2):
			if x % i == 0:
				isPrime = False
				break
		primes[x] = isPrime
	return primes

def offPrime(num):
	primes = off()
	if primes[num]:
		print num, "is a prime"
	else:
		i = 1
		while True:
			if primes[num + i]:
				print num, "is off by", i
				return
			if primes[num - i]:
				print num, "is off by", i
				return
			i+=1

offPrime(8)