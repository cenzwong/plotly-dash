# Concurrency & Parallelism in Python

- Concurrency is when processes are executed on a single processor by context switching, and they appear to be running simultaneously. 
- Parallelism is when processes are executed on multiple processors or cores and are actually running simultaneously.

# 1. Threading
```python
import threading
from threading import Thread

"""
Class Thread:
    # Target will be a callable function
    def __init__(self, target, name=None, args=90, kwargs={}):
        pass
"""
```
Thread class is key

You can construct a Thread. After constructing, all the function not yet running
```t.start()```

This will run the thread

Args must take in tuple, so if you are passing only one parameter, do this (1, ) 

# 2. Multiprocessing

# 3. Asyncio

# 4. Concurrent.futures

# 5. Other
## Trio
## Curio
## Rapids AI
## _thread
This is the python low level API of threading


## Reference
1. https://developer.hpe.com/blog/understanding-concurrency-in-python-part-1-threading
2. https://towardsdatascience.com/concurrency-in-python-e770c878ab53
3. https://realpython.com/python-concurrency/

- https://docs.python.org/3/library/ipc.html
- https://docs.python.org/3/library/concurrency.html

- [Tutorial: Santiago Basulto - Python Concurrency: from beginner to pro](https://www.youtube.com/watch?v=18B1pznaU1o)

# Sched
- https://towardsdatascience.com/scheduling-all-kinds-of-recurring-jobs-with-python-b8784c74d5dc
- running deferred jobs like with Linux ```at``` command
