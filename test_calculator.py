import pytest

from calculator import Calculator


@pytest.mark.parametrize("left,right,expected", [(2, 3, 5), (0, 4, 4), (-2, 5, 3)])
def test_add(left, right, expected):
    assert Calculator().add(left, right) == expected


def test_divide():
    assert Calculator().divide(9, 3) == 3


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        Calculator().divide(1, 0)
