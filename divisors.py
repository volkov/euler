def divisors(n):
    result = []
    for i in range(1,int(n**0.5)+1):
        if n % i == 0:
            result.append(i)
            j = n//i
            if (j!=i):
                result.append(j)
    return sorted(result)

def proper_divisors(n):
    return divisors(n)[:-1]
