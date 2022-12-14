books = [['qx',21],['lyr',21],['zyq',99]]
dict1 = dict(books)
print(type(dict1))
print(dict1)

print(dict1['qx'])

print(dict1.get('qx'))
print(dict1.get('lyr'))


print(dict1.items())
print(dict1.keys())
print(dict1.values())

