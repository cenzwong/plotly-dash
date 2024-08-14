```python
def convert_dict_to_tuples(_dict: dict) -> list:
    """
    Convert a dictionary of credit card bins to a list of tuples.

    Args:
        _dict (dict): Dictionary with bank names as keys and lists of BINs as values.

    Returns:
        list: List of tuples where each tuple contains a bank name and a BIN.

    Example
        key: [1,2],
        key2: [3]
        ->
        (key, 1),
        (key, 2),
        (key2, 3)
    """
    return [(key, value) for key, values in _dict.items() for value in values]
```