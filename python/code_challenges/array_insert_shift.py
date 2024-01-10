def insert_shift_array(input_array, value):

  length = len(input_array)
  center = length // 2
  if length % 2:
    center += 1

  left_array = input_array[0:center]
  right_array = input_array[center:length]

  left_array.append(value)
  new_array = left_array + right_array

  return new_array

print(insert_shift_array([1, 20, 9, 11, 52], 7))
