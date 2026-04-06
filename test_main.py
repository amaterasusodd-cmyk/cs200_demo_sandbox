import main
import pytest


def test_foo():
    assert main.foo(0, 0) == pytest.approx(1)
    assert main.foo(1, 0) == 1
    assert main.foo(0, 1) == 1
    assert main.foo(1, 1) == 1
