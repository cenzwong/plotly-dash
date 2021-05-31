
# Itertools

```py
import itertools

list1 = set(['home','home','away','home','away','home'])
list2 = set([1, 1, 1, 1, 2, 2])
list(itertools.product(list1, list2))
# [('home', 1), ('home', 2), ('away', 1), ('away', 2)]
```
