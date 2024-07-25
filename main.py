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

using the base 10 we have an increment of 1 when we arguments grows in power.
So, to have an increment of 2.7 we should change basis.

the base chosen by Gauss was e = 2.71
applying this property to the problem (find number of primes from 1 to n)
we have that the logarithm of 10^n base e gives the approximate distance from one prime to the other.
For example:
10 / p = ln(10)
10^2 / p = ln(10^2)

doing the inverse formula we can resolve the problem.

p = 10 / ln(10)
p = 10^2 / ln(10^2)
p = n / ln(n)

For small n number the uncertainty is pretty big try to use plot_primes() to see how the error decrease for bigger n
"""
import math
import matplotlib.pyplot as plt


# used to calculate primes
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2,int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True


# used to calculate primes
def create_primes(n):
    lst = []
    for i in range(n+1):
        if is_prime(i):
            lst.append(i)
        else:
            lst.append(0)
    #f = open('prime.txt','w')
    #f.write(str(lst))
    return lst


def distance_primes(lst: list, n: int):
    distances = {}
    loop = [10 ** i for i in range(1, round(math.log(n, 10)+1))]
    for i in loop:
        count = []
        for j in lst[:i]:
            if j != 0:
                count.append(j)
    #    print(len(count), i)
        mean = i / len(count)
        distances[str(i)] = mean
    return distances


def plot_primes(datas):
    x = list(datas.keys())[:-1]
    y = list(datas.values())
    y = [s-t for t, s in zip(y, y[1:])]
    print(y, x)
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    n_primes = 1000000
    primes = create_primes(n_primes)
    dist_primes = distance_primes(primes, n_primes)
    print(dist_primes)
    print(plot_primes(dist_primes))
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
