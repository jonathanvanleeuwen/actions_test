import pytest
from lib_template.basic_function import add, subtract


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(1, 2, 3, id="correct 1"),
        pytest.param(0, 2, 2, id="correct 2"),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(1, 2, -1, id="correct 1"),
        pytest.param(0, 2, -2, id="correct 2"),
    ],
)
def test_subtract(a, b, expected):
    assert subtract(a, b) == expected
