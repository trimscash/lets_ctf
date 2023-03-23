from Crypto.Util.number import *

p, q = getPrime(512), getPrime(512)
n = p * q
e = 65537
flag = b"flag{dummy}"

flag = bytes_to_long(flag)

c = pow(flag, e, n)

print("p =", p)
print("q =", q)
print("e =", e)
print("c =", c)
