# # What is the output of this code?
# #Before you clikc RUN, guess the output of each print statement!
# new_list = ['a', 'b', 'c']
# print(new_list[1])
# print(new_list[-2])
# print(new_list[1:3])
# new_list[0] = 'z'
# print(new_list)
#
# my_list = [1,2,3]
# bonus = my_list + [5]
# my_list[0] = 'z'
# print(my_list)
# print(bonus)


#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
# for value in picture:
#    for pixel in value:
#       if pixel ==0:
#           print(' ', end='')
#       else:
#           print('*', end='')
#    print('')

# print('Ala',end='@')
# print('Dominika')


# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# prev = 0
# for value in my_list:
#     outcome = value + prev
#     prev = outcome
#     print(outcome)

#
# some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']
#
# my_list=[]
# output_list=[]
# for value in some_list:
#     if value not in my_list:
#         my_list.append(value)
#     else:
#         output_list.append(value)
#
# print(output_list)

# 2 sposób:
# .count

# def counter(n1, n2):
#     def counter2():
#       return n1 + n2
#     return counter2
#
# total = counter(10,20)
#
# print(total())
#
# def checkDriverAge(age=0):
#     if int(age) < 18:
#         print("Sorry, you are too young to drive this car. Powering off")
#     elif int(age) > 18:
#         print("Powering On. Enjoy the ride!");
#     elif int(age) == 18:
#         print("Congratulations on your first year of driving. Enjoy the ride!")
#
# checkDriverAge()





















