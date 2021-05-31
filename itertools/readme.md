# Itertools
- https://realpython.com/python-itertools/
## import
```py
import itertools
```
## Two list return two unique combination
```py
list1 = set(['home','home','away','home','away','home'])
list2 = set([1, 1, 1, 1, 2, 2])
list(itertools.product(list1, list2)) # [('home', 1), ('home', 2), ('away', 1), ('away', 2)]
```
## Two list return two list elment by element
```py
list(zip([1, 2, 3], ['a', 'b', 'c'])) # [(1, 'a'), (2, 'b'), (3, 'c')]
```
