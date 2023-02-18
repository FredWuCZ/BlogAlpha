n = 100
p = 97
inv = [0 for i in range(n + 1)]
inv[1] = 1
for i in range(2, n + 1):
    inv[i] = (p - p // i) * inv[p % i] % p
print(inv[7])