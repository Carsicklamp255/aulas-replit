def is_on_list(list, item):
  count = 0
  for element in list:
    count += 1
    if element == item:
      print(f'rodou {count} vezes')
      return True

  print(f'rodou {count} vezes')
  return False

students = ["Jhon", "Maria", "José"]

print(is_on_list(students,'nathan'))