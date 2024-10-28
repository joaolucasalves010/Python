conjunto_a = {'a', 'b'}
conjunto_b = {'c', 'd'}

union_conjunto = conjunto_b.union(conjunto_a)
print(union_conjunto) 

array_union_conjunto = list(union_conjunto)
array_union_conjunto.sort()

print(array_union_conjunto) # >> a b c d 