#!/usr/bin/env python3

# -------
# imports
# -------
from Netflix import netflix_eval
from unittest import main, TestCase
from math import sqrt
from io import StringIO
from numpy import sqrt, square, mean, subtract

# -----------
# TestNetflix
# -----------

class TestNetflix (TestCase):

    # ----
    # eval
    # ----

    def test_eval_1(self):
        r = StringIO("10040:\n2417853\n1207062\n2487973\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10040:\n3.3\n3.4\n3.9\n0.90\n")

    def test_eval_2(self):
        r = StringIO("10:\n1952305\n1531863\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n3.3\n3.2\n0.25\n")

    def test_eval_3(self):
        r = StringIO("15702:\n1278813\n169485\n2196868\n2063829\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "15702:\n3.7\n3.8\n3.7\n3.6\n0.62\n")

    # ----
# main
# ----
if __name__ == '__main__':
    main()

""" #pragma: no cover
% coverage3 run --branch TestNetflix.py >  TestNetflix.out 2>&1
% coverage3 report -m                   >> TestNetflix.out
% cat TestNetflix.out
.
----------------------------------------------------------------------
Ran 1 test in 0.000s
OK
Name             Stmts   Miss Branch BrPart  Cover   Missing
------------------------------------------------------------
Netflix.py          27      0      4      0   100%
TestNetflix.py      13      0      0      0   100%
------------------------------------------------------------
TOTAL               40      0      4      0   100%
"""
