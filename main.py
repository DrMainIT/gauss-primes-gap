"""
the rapport between some number n and the numbers of primes that appears from 1 to n is something like this
n / p = q
p = primes
q = a quotient

Gauss found that every time the interval increase by a power of 10 the gap between the precedent result remains
approximately the same (2.7). For example if we calculate the rapport of a number n divided by the number of primes
contained in this interval n we get something like that
10/4 = 2,5
100/25 = 4,0
1000/168 = 6,0


and so on. Gauss found a correlation between primes and logarithm in this way

1) multiply by ten the left side we get an increment of approximately 2.7 on the right side
that is the concept behind the logarithm make a sum when the argument grows in power here an example:

f(x) = log(x) <=> 10^y = x

if x1 = 10 and x2 = 10^3

log(x1) = log(10) <=> 10^y = 10 ==> y = 1

log(x2) = log(10^3) <=> 10^y = 10^3 ==> y = 3

"""