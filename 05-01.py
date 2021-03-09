total = 0
count = 0

while True:
  num = input('Please enter a number (or done if finished): ')
  if num == 'done':
    break
  else:
    try:
      num = int(num)
      total += num
      count += 1
    except:
      print('Error, please enter a number')

if count > 0:
  print(total, count, total/count)

