def unique_list(l):
  num = []
  for a in l:
    if a not in num:
      num.append(a)
  return num
list = input("Enter the list of numbers:").split(" ")
list1= [int(x) for x in list]
print('unique elements are')
print(unique_list(list1))


