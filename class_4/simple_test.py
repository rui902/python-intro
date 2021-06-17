# test_with_pytest.py

import pytest


def test_always_passes():
    assert True


@pytest.mark.xfail(strict=True)
def test_fails_but_ok():
    assert False


# def test_always_fails():
#     assert False
