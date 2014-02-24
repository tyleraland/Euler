import math

# NOTE: pre-allocating memory for sieve dramatically reduces overhead
# compared to repeatedly appending
sum = 0
top = 2000000
sieve = [0] * (top+1)
i = 2 # Start at first odd number
while i < top:
    if sieve[i] == 0: # prime
        sum += i
        for x in [y*i for y in range(2, (top/i)+1)]:
            sieve[x] = 1 # Not prime
    i += 1
print(sum)
