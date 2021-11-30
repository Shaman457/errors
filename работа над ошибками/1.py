import random
a = [random.randint(1,15) for i in range(random.randint(1,20))]
print(a)
print(a[0], a[-1])
s = 1
for i in a:
    s*=i
print(s)