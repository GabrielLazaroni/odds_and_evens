while True:

  try:
    value = int(input('digite um valor:'))
    if value % 2 == 0:
      print('even number')
    else:
      print('odd number')
  except:
    print('type numbers')