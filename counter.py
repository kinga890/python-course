my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('1 sposób')
prev = None

for value in my_list:
    if prev is None:
        result = value
        prev = value
    else:
        result = prev + value
        prev = result

    print(result)
print(result)  # żeby wyświetlić tylko końcową sumę

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('2 sposób')
prev = my_list[0]
print(my_list[0])
for value in my_list[1:]:
    result = prev + value
    prev = result
    print(result)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
my_set=set()
prev = None

for value in my_list:
    if prev is None:
        result = value
        prev = value
        my_set.add(value)

    else:
        result = prev + value
        prev = result
        my_set.add(result)
list = list(my_set)
list.sort()
print(list)

