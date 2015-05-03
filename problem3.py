#
# Problem 3:
#
# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?
#
import math


number = 600851475143
sqrt_number = int(math.sqrt(number))

prime_factor = []

for x in xrange(2,sqrt_number):

	if number%x==0:
		prime_factor.append(x)
		number /= x

print "Problem 3:",prime_factor[-1]