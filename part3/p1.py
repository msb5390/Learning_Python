S = 'this is a string!'

# Part (a)
#for char in S:
#    print(ord(char), end=' ')
#print()

# Part (b)
#c_sum = 0
#for char in S:
#    c_sum += ord(char)
#print(c_sum)

# Part (c)
#code_list = []
#for char in S:
#    code_list.append(ord(char))
#print(code_list)

# Part (c) testing map:
#code_list = map(ord, S)
#print(list(code_list))

# Part (c) using list comprehension
print([ord(c) for c in S])
