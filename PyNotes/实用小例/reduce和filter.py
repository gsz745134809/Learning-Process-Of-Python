# reduce用于进行归纳计算：
from functools import reduce
product = reduce((lambda x,y:x*y), [1,2,3,4])
print(product)
# 24

# filter对数组进行过滤：
number_list = range(-5,5)
less_than_zero = list(filter(lambda x:x<0,number_list))
print(less_than_zero)
# [-5, -4, -3, -2, -1]