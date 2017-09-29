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
        r= StringIO("14307:\n2131996\n100797\n1081043")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(w.getvalue(), "14307:\n3.56\n4.76\n4.91\n")

    def test_eval_2(self):
        r= StringIO("14308:\n1784102\n1288561\n1719881")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(w.getvalue(), "14308:\n3.02\n2.99\n2.91\n")

    def test_eval_3(self):
        r= StringIO("14309:\n1048550\n739050\n1901270")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(w.getvalue(), "14309:\n3.10\n3.43\n3.15\n")

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
