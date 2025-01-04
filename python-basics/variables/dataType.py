# python have 8 data types
# 1) text type : str
# 2) Numeric Type: int, float, complex
# 3) sequance Type  : list , tuple, range
# 4) Boolean type : bool
# 5) Mapping Type: dict
# 6) set Type : set, frozenset
# 7 binary Types : bytes, bytesArray, memoryview
# 8) NoneType : NoneTpe 
x=10
print(type(x))
x=10.45
print(type(x))

a,b,c,a = [10,3,4,5]
t=isinstance(a, int)
p=[90,7,8]
q=[90, 7,8]
del a


print(b,c, t, ''=='', p==q, id(p), id(q))