import main
import pytest


@pytest.mark.parametrize(
        ('input_x', 'input_y', 'expected'),
        (
            (0, 0, 1),
            (1, 0, 1),
            (0, 1, 1),
            (1, 1, 2)
        )
)
def test_foo(input_x, input_y, expected):
    # assert main.foo(0, 0) == pytest.approx(1)
    # assert main.foo(1, 0) == 1
    # assert main.foo(0, 1) == 1
    # assert main.foo(1, 1) == 1
    assert main.foo(input_x, input_y) == expected

@pytest.mark.parametrize(
    ('input_x','expected'),
    (
        (0,0),
        (1,5),
        (2,10),
        (10,50)
    )
)
def test_bar(input_x, expected):
    assert main.bar(input_x) == expected