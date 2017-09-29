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
        r = StringIO("16070:\n1952549\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "16070:\n3.1\n0.80\n")
    
    def test_eval_2(self):
        r = StringIO("2007:\n2404189\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "2007:\n2.9\n2.00\n")
    
    def test_eval_3(self):
        r = StringIO("3142:\n1989364\n1671223\n355591\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "3142:\n3.1\n3.0\n2.9\n1.41\n")
    '''

    def test_eval_1(self):
        r = StringIO("10040:\n2417853\n1207062\n2487973\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10040:\n3.3\n3.2\n3.5\n1.55\n")
    def test_eval_2(self):
        r = StringIO("10851:\n43429\n259145\n114662\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10851:\n3.6\n3.7\n3.9\n1.31\n")
    def test_eval_3(self):
        r = StringIO("2043:\n1417435\n2312054\n462685\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "2043:\n3.7\n2.3\n3.7\n0.87\n")

    '''
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
