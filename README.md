# Nice Parametrize

Usage example:
```python
from nice_parametrize import parametrize

@parametrize(["a", "b", "result"], {
    "equal": [1, 1, True],
    "unequal": [1, 2, False],
})
def my_test(a, b, result):
    assert (a == b) is result
```

A small Python snippet that makes `pytest.mark.parametrize` a little nicer to use.

`pytest.mark.parametrize` has a nice feature called `ids` that allows you to name your argument lists.
This is very useful for stating the intention of the tested case. 
But the problem is that the names are given in a separate parameter, `ids`, 
so it is not easy to see at a glance which arguments match which case:

```python
import pytest

@pytest.mark.parametrize(["a", "b", "result"], [
    [1, 1, True], 
    [1, 2, False]], 
ids=["equal", "unequal"])
def my_test(a, b, result):
    assert (a == b) is result
```

This might get very cumbersome with a long parameter list and a lot of cases.
So instead, `nice_parametrize` allows you to pass in a `dict` that 
maps between the ID of the argument list to the list itself.
This way it is clear which case match which arguments, 
and it is easier to understand and debug your test.

Also supports additional keyword arguments to be passed to the underlying `pytest.mark.parametrize`.