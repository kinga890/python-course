my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print('sposób A')
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

print('sposób B')
prev = my_list[0]
print(my_list[0])
for value in my_list[1:]:
    result = prev + value
    prev = result
    print(result)

print('sposób C')

print('KACPER PRZECZYTAJ TO ROZIWĄZANIE')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
counter = 0
for value in my_list:
    counter=counter + value
    print(counter)


# wynik jako lista

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result_list=list()

prev = None

for value in my_list:
    if prev is None:
        result = value
        prev = value
        result_list.append(value)  #dodaję element do końcowej listy

    else:
        result = prev + value
        prev = result
        result_list.append(result)   #dodaję element do końcowej listy
print(type(result_list))
print((result_list))

