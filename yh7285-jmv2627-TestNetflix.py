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
        #print(w.getvalue())
        self.assertEqual(
            w.getvalue(), "10040:\n3.1\n2.9\n3.4\n0.83\n")
            #w.getvalue(), "10040:\n2.4\n2.4\n2.4\n0.90\n")
    

    def test_eval_2(self): #running more than one movie, and same movie twice
        r = StringIO("10040:\n2417853\n1207062\n2487973\n10040:\n2417853\n1207062\n2487973\n")
        w = StringIO()
        netflix_eval(r, w)
        #print(w.getvalue())
        self.assertEqual(
            w.getvalue(), "10040:\n3.1\n2.9\n3.4\n10040:\n3.1\n2.9\n3.4\n0.83\n")

    def test_eval_3(self): #same customer multiple times
        r = StringIO("10040:\n2417853\n2417853\n2487973\n")
        w = StringIO()
        netflix_eval(r, w)
        #print(w.getvalue())
        self.assertEqual(
            w.getvalue(), "10040:\n3.1\n3.1\n3.4\n0.83\n")


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
