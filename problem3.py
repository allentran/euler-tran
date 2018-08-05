# Use idea that every integer is product of primes.  Find a small prime factor, and then recursively find the rest.

factorize_num = 600851475143

odd_num = 3
while True:
    if factorize_num % odd_num == 0:
        print(factorize_num/odd_num, odd_num
        factorize_num = factorize_num/odd_num
        odd_num = 3
    if odd_num > factorize_num/2:
        break
    odd_num += 2
