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
        r = StringIO("10044:\n414171\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10044:\n3.87\n0.87\n")

    def test_eval_2(self):
        r = StringIO("9997:\n2179700\n1347835\n765578\n2328701\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "9997:\n3.71\n3.88\n3.81\n4.00\n1.04\n")

    def test_eval_3(self):
        r = StringIO("9998:\n1288730\n2536567\n1107317\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "9998:\n2.81\n3.04\n3.66\n0.95\n")

    def test_eval_4(self):
        r = StringIO("9999:\n1473765\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "9999:\n1.27\n0.72\n")


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
