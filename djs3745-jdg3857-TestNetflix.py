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
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.75\n4.0\n3.0\n5.0\n5.0\n0.44\n")

    def test_eval_1(self):
        r = StringIO("10:\n1952305\n1531863\n1000:\n2326571\n977808\n1010534\n1861759\n79755\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10:\n3.0\n3.0\n1000:\n3.0\n3.0\n2.0\n5.0\n4.5\n0.37\n")

    def test_eval_1(self):
        r = StringIO("10609:\n316130\n445777\n681379\n1061:\n2294397\n1363135\n457330\n1557262\n10610:\n1045221\n734556\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10609:\n4.0\n4.0\n5.0\n1061:\n5.0\n3.5\n5.0\n3.0\n10610:\n2.0\n3.5\n0.74\n")

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
