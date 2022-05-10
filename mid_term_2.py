lst = ['H', 'e', 'l', 'l', 'o', ' ', 'I', 'a', 'T']

lst[7] = 'o'

print(lst)

lst.append('?')

print(lst)

print(len(lst))

print(lst[0] + lst[1] + lst[2] + lst[3] + lst[4] + lst[5] + lst[6] + lst[7] + lst[8] + lst[9])

lst.sort(reverse=True)
print(lst)