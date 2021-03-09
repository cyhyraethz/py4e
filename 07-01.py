fname = input('Please enter file name: ')

try:
  fhand = open(fname)
except:
  print('Error, file not found.')
  quit()

for line in fhand:
  print(line.upper().rstrip())


