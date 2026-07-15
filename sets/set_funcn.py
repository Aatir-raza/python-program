# len/sum/min/max/soerted
s={3,1,4,5,2,7}
print(len(s))
print(sum(s))
print(min(s))
print(max(s))
print(sorted(s,reverse=True))

# union-update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
# s1|s2
s1.union(s1)
s1.update(s2)
print(s1)
print(s2)
# intersection|intersecton _update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
# s1|s2
s1.intersection(s2)
s1.intersection_update(s2)
print(s1)
print(s2)
# difference /differnce_update 
s1={1,2,3,4,5}
s2={4,5,6,7,8}
# s1|s2
s1.union(s1)
s1.update(s2)
print(s1)
print(s2)
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.difference(s1)
s1.difference_update(s2)
print(s1)
print(s2)
# symmetric _differnce /symmetric _diiferenece #_update
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.symmetric_difference(s1)
s1.symmetric_difference_update(s2)
print(s1)
print(s2)
# isdisjoint/is subset/issuperset
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.isdisjoint(s2)
print(s1)
# is subset
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s2.issubset(s1)
# superset
s1={1,2,3,4,5}
s2={4,5,6,7,8}
s1.issuperset(s2)
# copy
s1={1,2,3}
s2={3,4,5}
print(s1)
print(s2)



