# python3

def sum(list):
  if list == []:
    return 0
  list_ = list[0]
  print(list_)
  return list_ + sum(list[1:])

list = [1, 2, 3, 4, 5]

print(sum(list))
