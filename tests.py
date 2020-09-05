import pytest
from nice_parametrize import parametrize


@parametrize(["a", "b", "result"], {
    "equal": [1, 1, True],
    "unequal": [1, 2, False],
})
def test_nice_parametrize(a, b, result):
    assert (a == b) is result


@pytest.fixture
def my_fixture():
    return 1


@parametrize(["a", "result"], {
    "equal": [1, True],
    "unequal": [2, False]
})
def test_with_fixture(a, my_fixture, result):
    assert (a == my_fixture) is result
