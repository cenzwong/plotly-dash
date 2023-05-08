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
[(x,y) for x in list1 for y in list2] # [('home', 1), ('home', 2), ('away', 1), ('away', 2)]
list(((x,y) for x in list1 for y in list2)) # [('home', 1), ('home', 2), ('away', 1), ('away', 2)]
```
## Two list return two list elment by element
```py
list(zip([1, 2, 3], ['a', 'b', 'c'])) # [(1, 'a'), (2, 'b'), (3, 'c')]
```
```py
import itertools

Year_option = range(_last_year, _this_year+1)
Month_option = range(12)
Day_option = [1]

# generate all possible combinations of elements from the three groups
combinations = list(itertools.product(Year_option, Month_option, Day_option))

# print all the combinations
for comb in combinations:
    print(comb)
```