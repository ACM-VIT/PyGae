l={1:"python",2:"c",3:"ruby",4:"java"}

b=l.copy()
print(b)

l.clear()
print(l)

flag=[1,2,3,4,5]
l=l.fromkeys(flag,7)
print(l)

print(l.has_key(7))
print(l.has_key(1))

print(l.get(1,0))
print(l.get(7,0))

print(l.items())

print(l.values())

print(l.keys())

print(l.setdefault(7,0))
print(l)

flag_dict={10:'javascript',11:'php'}
l.update(flag_dict)
print(l)

