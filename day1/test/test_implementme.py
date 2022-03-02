import pytest

from day1.implementme import categorize_triangle


@pytest.mark.parametrize("a, b, c", [(3, 4, 5), (5, 4, 3), (13, 12, 5)])
def test_categorize_triangle_return_直角三角形(a, b, c):
    assert categorize_triangle(a, b, c) == "直角三角形"


def test_categorize_triangle_return_正三角形():
    assert categorize_triangle(3, 3, 3) == "正三角形"


def test_categorize_triangle_return_二等辺三角形():
    assert categorize_triangle(3, 3, 2) == "二等辺三角形"


def test_categorize_triangle_return_鋭角三角形():
    assert categorize_triangle(9, 6, 8) == "鋭角三角形"


def test_categorize_triangle_return_鈍角三角形():
    assert categorize_triangle(3, 4, 6) == "鈍角三角形"


@pytest.mark.parametrize(
    "a, b, c", [(3, 3, 7), (3, 3, 6), (0, 3, 3), (-3, 4, 5), (-3, -3, -3)]
)
def test_categorize_triangle_return_None(a, b, c):
    assert categorize_triangle(a, b, c) is None


if __name__ == "__main__":
    pytest.main()
