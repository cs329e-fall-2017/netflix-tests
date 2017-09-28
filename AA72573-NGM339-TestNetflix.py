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
        r = StringIO("1:\n30878\n2647871\n1283744\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.81871003558\n3.52771003558\n3.45971003558\n0.39\n")

    def test_eval_2(self):
        r = StringIO("10:\n1952305\n1531863\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n2.98071003558\n2.71571003558\n0.20\n")

    def test_eval_3 (self):
        r = StringIO("1000:\n2326571\n977808\n1010534\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "1000:\n3.25271003558\n2.94171003558\n2.70671003558\n0.43\n")

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
