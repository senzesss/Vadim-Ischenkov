path = 'C:\Thecode\12edia\kek.txt'
list1 = path.split('\\')
print(list1)
if len(list1) <= 1:
  print('\\')
else:
  print(list1[0])
