# Nice Parametrize

```python
from nice_parametrize import parametrize

@parametrize(["a", "b", "result"], {
    "equal": [1, 1, True],
    "unequal": [1, 2, False],
})
def my_test(a, b, result):
    assert (a == b) is result
```