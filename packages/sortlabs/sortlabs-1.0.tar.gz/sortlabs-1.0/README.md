
## Usage

Here are some examples of how to use the functions in the `sortlabs` module:

```python
from sortlabs import quick_sort, group_arrays, merge_and_sort_arrays, find_max, find_min, count_occurrences, remove_duplicates, reverse_array

# Quick sort
sorted_arr = quick_sort([5, 2, 8, 1, 9])
print(sorted_arr)  # Output: [1, 2, 5, 8, 9]

# Group arrays
grouped_arr = group_arrays([1, 3, 5], [2, 4, 6])
print(grouped_arr)  # Output: [1, 2, 3, 4, 5, 6]

# Merge and sort arrays
merged_and_sorted_arr = merge_and_sort_arrays([1, 3, 5], [2, 4, 6])
print(merged_and_sorted_arr)  # Output: [1, 2, 3, 4, 5, 6]

# Find maximum and minimum values
max_val = find_max([5, 2, 8, 1, 9])
print(max_val)  # Output: 9
min_val = find_min([5, 2, 8, 1, 9])
print(min_val)  # Output: 1

# Count occurrences
count = count_occurrences([1, 2, 3, 2, 1], 2)
print(count)  # Output: 2

# Remove duplicates
unique_arr = remove_duplicates([1, 2, 3, 2, 1])
print(unique_arr)  # Output: [1, 2, 3]

# Reverse array
reversed_arr = reverse_array([1, 2, 3, 4, 5])
print(reversed_arr)  # Output: [5, 4, 3, 2, 1]
