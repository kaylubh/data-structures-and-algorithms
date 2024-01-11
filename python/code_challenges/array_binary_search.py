def binary_search(sorted_array, search_key):

  low_index = 0
  high_index = len(sorted_array) - 1

  while low_index <= high_index:

    mid_index = (low_index + high_index) // 2
    mid_value = sorted_array[mid_index]

    if search_key == mid_value:
      return mid_index

    if search_key < mid_value:
      high_index = mid_index - 1
    elif search_key > mid_value:
      low_index = mid_index + 1

  return -1

print(binary_search([1, 2, 3, 5, 6, 7], 4))
