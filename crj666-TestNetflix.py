#!/usr/bin/env python3

# -------
# imports
# -------
from Netflix import netflix_eval, get_average_rating, create_cache
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
            w.getvalue(), "10040:\n2.9\n2.8\n3.4\n0.79\n")

    def test_eval_2(self):
        r = StringIO("10040:\n2417853\n1207062\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10040:\n2.9\n2.8\n0.90\n")

    def test_eval_3(self):
        r = StringIO("10040:\n2417853\n")
        w = StringIO()
        netflix_eval(r, w)
        self.assertEqual(
            w.getvalue(), "10040:\n2.9\n1.00\n")

    # ------------------
    # get_average_rating
    # ------------------

    def test_get_avg_rating_1(self):
        r = StringIO("10040:\n2417853\n1207062\n2487973\n")
        w = StringIO()
        average_customer_rating = create_cache("cache-averageCustomerRating.pickle")
        avg = get_average_rating(average_customer_rating)
        self.assertEqual(str(avg)[:3], "3.6")

    def test_get_avg_rating_2(self):
        r = StringIO("10040:\n2417853\n1207062\n2487973\n")
        w = StringIO()
        average_movie_rating = create_cache("cache-averageMovieRating.pickle")
        avg = get_average_rating(average_movie_rating)
        self.assertEqual(str(avg)[:3], "3.2")

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
