#!/usr/bin/env python3

# -------
# imports
# -------
from Netflix import netflix_eval, get_prediction
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
        r = StringIO("3712:\n1143110\n847553\n834\n55878\n249411\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "3712:\n2.926\n3.133\n3.065\n2.803\n3.004\n\n0.67\n")

    def test_eval_1(self):
        r = StringIO("4567:\n148434\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "4567:\n2.007\n0.00\n")

    def test_eval_1(self):
        r = StringIO("1:\n30878\n2647871\n1283744\n2488120\n317050\n10:\n1952305\n1531863\n1000:\n2326571\n977808\n1010534\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "1:\n3.799\n3.454\n3.573\n4.85\n3.837\n10:\n2.983\n2.724\n1000:\n3.265\n2.955\n2.693\n0.51\n")




    def test_predict(self):
        cid = 459852
        mid = 16412
        result = get_prediction(mid, cid)
        self.assertEqual(result, 2.905)

    def test_predict_2(self):
        cid = 1952305
        mid = 10
        result = get_prediction(mid, cid)
        self.assertEqual(result, 2.983)

    def test_predict_3(self):
        cid = 1952305
        mid = 256
        result = get_prediction(mid, cid)
        self.assertEqual(result, 3.288)

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
