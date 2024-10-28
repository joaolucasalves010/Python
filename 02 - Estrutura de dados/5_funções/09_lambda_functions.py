def sum(x, y):
  return x + y

print(sum(5, 4))

sum2 = lambda x, y: x + y
print(sum2(5, 4))

def my_map(function, int):
  result = []
  for items in int:
    new_item = function(items)
    result.append(new_item)
  return result

nums = [1, 2, 3, 4]

my_arr_cubed = my_map(lambda x: x**3, nums)
print(my_arr_cubed)