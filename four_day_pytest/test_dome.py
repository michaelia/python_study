#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
func = lambda x :  x + 1


class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x
    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


if __name__ == 'main()':
    pytest.main('-q test_dome.py')