#
# Problem 3:
#
# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.
#

palind = 0
for x in xrange(99,1001):
	for y in xrange(99,1001):

		prod = str(x*y)
		prod_rev = prod[::-1]
		if prod == prod_rev and x*y > palind:
			palind = x*y

print "Problem 3:",palind
