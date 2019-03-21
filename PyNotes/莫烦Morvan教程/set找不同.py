# set 基本 

# Set 最主要的功能就是寻找一个句子或者一个 list 当中不同的元素.
char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
sentence = 'Welcome Back to This Tutorial'
print(set(char_list))
# {'b', 'd', 'a', 'c'}
print(set(sentence))
# {'l', 'm', 'a', 'c', 't', 'r', 's', ' ', 'o', 'W', 'T', 'B', 'i', 'e', 'u', 'h', 'k'}
print(set(char_list+ list(sentence)))
# {'l', 'm', 'a', 'c', 't', 'r', 's', ' ', 'd', 'o', 'W', 'T', 'B', 'i', 'e', 'k', 'h', 'u', 'b'}


# 添加元素 

# 定义好一个 set 之后我们还可以对其添加需要的元素, 使用 add 就能添加某个元素. 但是不是每一个东西都能添加, 比如一个列表.
unique_char = set(char_list)
unique_char.add('x')
# unique_char.add(['y', 'z']) this is wrong
print(unique_char)
# {'x', 'b', 'd', 'c', 'a'}


# 清除元素或 set 

# 清除一个元素可以用 remove 或者 discard, 而清除全部可以用 clear.
unique_char.remove('x')
print(unique_char)
# {'b', 'd', 'c', 'a'}
unique_char.discard('d')
print(unique_char)
# {'b', 'c', 'a'}
unique_char.clear()
print(unique_char)
# set()


# 筛选操作 

# 我们还能进行一些筛选操作, 比如对比另一个东西, 看看原来的 set 里有没有和他不同的 (difference). 或者对比另一个东西, 看看 set 里有没有相同的 (intersection).
unique_char = set(char_list)
print(unique_char.difference({'a', 'e', 'i'}))
# {'b', 'd', 'c'}
print(unique_char.intersection({'a', 'e', 'i'}))
# {'a'}