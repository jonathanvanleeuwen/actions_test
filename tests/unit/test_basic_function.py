import pytest
from actions_test.basic_function import add


@pytest.mark.parametrize(
    "a, b, expected",
    [
        pytest.param(1, 2, 3, id="correct 1"),
        pytest.param(0, 2, 2, id="correct2"),
        pytest.param(1, 2, 4, id="incorrect throw error"),
    ],
)
def test_add(a, b, expected):
    assert add(a, b) == expected
