import functools

n = 8939011
e = 35
p = 2957
q = 3023
phi = (p - 1) * (q - 1)
d = 510459


# for i in range(n):
#	if (i*e)%phi == 1:
#		print(i)

def encrypt(number):
    return (number ** e) % n


def decrypt(number):
    return (number ** d) % n


print(encrypt(1234567))
print(decrypt(7654321))


def factors(n):
    return set(functools.reduce(list.__add__,
                                ([i, n // i] for i in range(1, int(n ** 0.5) + 1) if n % i == 0)))
