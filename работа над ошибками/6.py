import random
n = 5
m = 5
mat = [[random.randint(1,9) for g in range(m)] for i in range(n)]
for i in mat:
    print(f"\t{i}")
diagonal = [mat[i][g] for i in range(n) for g in range(m) if i==g]
print(diagonal)
k = int(input())
string = [mat[k-1][i] for i in range(n)]
print(string)