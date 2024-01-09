def reverse_array(array_to_reverse):

  length = 0
  for value in array_to_reverse:
    length += 1

  reversed_array = []

  index = length - 1
  while index >= 0:
    reversed_array.append(array_to_reverse[index])
    index -= 1

  return reversed_array

test_array = [4, 9, 2, 5]
reverse_test = reverse_array(test_array)
print(reverse_test)
