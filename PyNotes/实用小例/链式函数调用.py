def product(a, b):
	return a * b

def add(a, b):
	return a + b

b = True

print((product if b else add)(5, 7))

b = False 

print((product if b else add)(5, 7))

# [out]:
# 35
# 12
