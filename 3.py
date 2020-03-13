
def solve(n):
    largestPrimeFactor = 0

    if n % 2 == 0:
        largestPrimeFactor = 2;
        while n % 2 == 0:
            n /= 2

    if n % 3 == 0:
        largestPrimeFactor = 3;
        while n % 3 == 0:
            n /= 3

    multOfSix = 6;
    while multOfSix - 1 <= n:
        if n % (multOfSix - 1) == 0:
            largestPrimeFactor = multOfSix - 1
            while n % largestPrimeFactor == 0:
                n /= largestPrimeFactor 

        if n % (multOfSix + 1) == 0:
            largestPrimeFactor = multOfSix + 1
            while n % largestPrimeFactor == 0:
                n /= largestPrimeFactor
            
        multOfSix += 6;

    print(largestPrimeFactor)

solve(600851475143)
