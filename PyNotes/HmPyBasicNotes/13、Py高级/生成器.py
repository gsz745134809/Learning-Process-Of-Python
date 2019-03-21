def simple_generator_function():
    yield 1
    yield 2
    yield 3

for value in simple_generator_function():
    print(value)


# 输出结果
# 1
# 2
# 3

our_generator = simple_generator_function()
next(our_generator)
# 1
next(our_generator)
# 2
next(our_generator)
# 3

# 生成器典型的使用场景譬如无限数组的迭代
def get_primes(number):
    while True:
        if is_prime(number):  # 如果是素数
            yield number
        number += 1
