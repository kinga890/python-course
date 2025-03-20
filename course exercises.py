# What is the output of this code?
#Before you clikc RUN, guess the output of each print statement!
new_list = ['a', 'b', 'c']
print(new_list[1])
print(new_list[-2])
print(new_list[1:3])
new_list[0] = 'z'
print(new_list)

my_list = [1,2,3]
bonus = my_list + [5]
my_list[0] = 'z'
print(my_list)
print(bonus)


# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

for value in picture:
   for pixel in value:
      if pixel ==0:
          print(' ', end='')
      else:
          print('*', end='')
   print('')

print('Ala',end='@')
print('Dominika')


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

prev = 0
for value in my_list:
    outcome = value + prev
    prev = outcome
    print(outcome)


some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

my_list=[]
output_list=[]
for value in some_list:
    if value not in my_list:
        my_list.append(value)
    else:
        output_list.append(value)

print(output_list)

# 2 sposób:
# .count

def counter(n1, n2):
    def counter2():
      return n1 + n2
    return counter2

total = counter(10,20)

print(total())

def checkDriverAge(age=0):
    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!");
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")

checkDriverAge()



def my_func(*args, **kwargs):
    total = 0
    for value in kwargs.values():
        total+=value
    return sum(args) + total

print(my_func(1,2,3,4,5, num1=10, num2=5 ))

my_list=[]

def highest_even(args):
    for value in args:
        if value % 2 == 0:
            my_list.append(value)
    return (max(my_list))


print((highest_even([2,6,8,32,11,45,17,18])))

total = 0

def count(total):
    total+=1
    return total

print(count(count(count(total))))  #=3

print(total)    #=0














