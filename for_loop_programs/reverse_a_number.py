n = 123
rev = 0

for _ in range(len(str(n))):
    rev = rev * 10 + n % 10
    n //= 10

print(rev)
