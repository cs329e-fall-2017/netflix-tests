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
        r = StringIO(
            "1:\n30878\n2647871\n1283744\n2488120\n317050\n17300:\n1762631\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.9\n3.5\n3.5\n4.9\n3.9\n17300:\n1.0\n0.68\n")

    def test_eval_2(self):
        r = StringIO(
            "10:\n1952305\n1531863\n1000:\n2326571\n977808\n1010534\n1861759\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n3.0\n2.7\n1000:\n3.3\n3.0\n2.7\n4.7\n0.34\n")

    def test_eval_3(self):
        r = StringIO(
            "10004:\n1737087\n1270334\n1262711\n10008:\n1813636\n2048630\n930946\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10004:\n5.0\n4.2\n4.4\n10008:\n4.9\n3.4\n3.7\n0.96\n")
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
