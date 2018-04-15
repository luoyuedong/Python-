import itertools

s = [1,2,3]
a = list(itertools.combinations(s,2)) #组合
print(a)
b = list(itertools.permutations(s,2)) #排列
print(b)