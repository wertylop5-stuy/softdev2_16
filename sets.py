def union(a, b):
	print "sets"
	print a, b
	return a + [ x for x in b if x not in a ]

def intersection(a, b):
	print "sets"
	print a, b
	return [ x for x in a if x in b ]

def set_difference(a, b):
	print "sets"
	print a, b
	return [ x for x in a if x not in b ]

def symm_difference(a, b):
	print "sets"
	print a, b
	return set_difference(union(a, b), intersection(a, b))

def cart_product(a, b):
	print "sets"
	print a, b
	return [ [x, y] for x in a for y in b]

print "intersection"
print intersection([0, 1, 2], [2, 3, 4])
print intersection([0, 1], [2, 3, 4])
print intersection([2, 1, 4], [2, 3, 4])
print "\n"

print "union"
print union([0, 1, 2], [2, 3, 4])
print union([0, 1], [2, 3, 4])
print union([2, 1, 4], [2, 3, 4])
print "\n"

print "set_difference"
print set_difference([0, 1, 2], [2, 3, 4])
print set_difference([0, 1], [2, 3, 4])
print set_difference([2, 1, 4], [2, 3, 4])
print set_difference([2, 3, 4], [0, 1, 2])
print set_difference([2, 3, 4], [0, 1])
print set_difference([2, 3, 4], [2, 1, 4])
print "\n"

print "cart_product"
print cart_product([0, 1, 2], [2, 3, 4])
print cart_product([0, 1], [2, 3, 4])
print cart_product([2, 1, 4], [2, 3, 4])
print "\n"

