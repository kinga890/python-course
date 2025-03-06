

#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# wiem że to rozwiązanie to mega syzyf ale przynajmniej działa, zaraz postaram się to zoptymalizować

my_list= [
  [],
  [],
  [],
  [],
  [],
  []
]

for value in picture[0]:
  if value == 0:
    value = ' '
  else:
    value = "*"
  my_list[0].append(value)


for value in picture[1]:
  if value == 0:
    value = ' '
  else:
    value = "*"
  my_list[1].append(value)

for value in picture[2]:
  if value == 0:
      value = ' '
  else:
      value = "*"
  my_list[2].append(value)


for value in picture[3]:
  if value == 0:
    value = ' '
  else:
    value = "*"
  my_list[3].append(value)


for value in picture[4]:
  if value == 0:
    value = ' '
  else:
    value = "*"
  my_list[4].append(value)


for value in picture[5]:
  if value == 0:
    value = ' '
  else:
    value = "*"
  my_list[5].append(value)

for tree in my_list:
  print(tree)

