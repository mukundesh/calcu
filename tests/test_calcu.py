#!/usr/bin/env python
"""Tests for `calcu` package."""

from calcu import add, sub


def test_add():
    """Sample pytest test function to test add."""
    assert add(1, 3) == 4
    assert add(1, 2) == 3


def test_sub():
    """Sample pytest test function to test sub."""
    assert sub(3, 1) == 2
    assert sub(2, 1) == 1
