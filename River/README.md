# River - Machine learning for data streams in Python

[RiverML.xyz](https://riverml.xyz/latest/)

## Import CSV

[Reading Data](https://riverml.xyz/latest/user-guide/reading-data/)

Recap

In ```river```, the features of a sample are stored inside a dictionary, which in Python is called a ```dict``` and is a native data structure. In other words, we don't use any sophisticated data structure, such as a ```numpy.ndarray``` or a ```pandas.DataFrame```.

In fact, the ```stream.iter_csv``` method from ```river``` is just a wrapper on top of ```csv.DictReader``` that adds a few bells and whistles.

Note that when we say "loaded", we don't mean that the actual data is read from the disk. On the contrary, the dataset is a streaming data that can be iterated over one sample at a time. In Python lingo, it's a [generator](https://realpython.com/introduction-to-python-generators/).


```python

from river import stream

X_y = stream.iter_csv(dataset.path)
x, y = next(X_y)
# or
x, y = next(iter(dataset))

for x, y in dataset:
    # do sth

```