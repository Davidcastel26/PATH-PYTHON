# symetric_difference(set2) todo lo que no sea la interseccion
set1 = {1,2,3,4,5,6}
set2 = {3,4,5,6,7,8}
set3 = {3,4}
syme_diff = set1.symmetric_difference(set2)

# .issubset(set2) es subconjunto de  set 1 retorna True or False
subset = set1.issubset(set3) #true

# issuperset(set2 )
superset = set1.issuperset(set2)
superset = set1.issuperset(set3)