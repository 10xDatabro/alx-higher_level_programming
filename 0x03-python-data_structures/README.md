0x03.Python - Data Structures: Lists, Tuples


To compare objects **based on their values**, Python's equality operators `==` are employed.
`==` returns `True` if two objects, have the same value, and return `False` if both have different value
```python
# This script prints True because the value of a is the same value for b 
a = 5
b = 5

if a == b:
    print("True")
else: 
    print("False")
```

`is` and `is not` operators are Python identity operators. They are used to compare objects **based on their identity**. `is` evaluates to `True` when the variables on its left side and its right side point to the exact same object. Otherwise, it would return `False`.
```python
# This script prints True because the identity of my_list is list
my_list = [1,2,3,4]

if my_list is list:
    print("True")
else:
    print("False")#True 

True
```

### How to print element of a list of lists(Matrix) with Python
You need to write your code to dynamically know the number of rows (number of lists inside the list) 
and the number of columns (number of elements in the lists inside the list). 
The row number will control an outer loop that will loop through the number of lists inside the list 
while the column number will control a nested loop that will loop through the number of elements in each
of the lists inside the list.

Lets say we have a list of lists `matrix`
```python
matrix = [
	[1, 2, 3, 4],
	[5, 6, 7, 8],
	[8, 9, 10, 11]
]
```
we can print the matrix with this 
```python
row_number = 3
column_number = 4
```
see [6-print_matrix_integer.py](https://github.com/10xDatabro/alx-higher_level_programming/blob/master/0x03-python-data_structures/6-print_matrix_integer.py] for code implementation)
