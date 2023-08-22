# Task 1

# Pick your solution to one of the exercises in this module.
# Design tests for this solution and write tests using unittest library.

from unittest import TestCase, main
from mathematician import Mathematician


class TestMathematician(TestCase):
    def setUp(self):
        self.mathematician = Mathematician()

    def test_square_nums(self):
        self.assertEqual(self.mathematician.square_nums(
            [7, 11, 5, 4]), [49, 121, 25, 16])

    def test_remove_positives(self):
        self.assertEqual(self.mathematician.remove_positives(
            [26, -11, -8, 13, -90]), [-11, -8, -90])

    def test_filter_leaps(self):
        self.assertEqual(self.mathematician.filter_leaps(
            [2001, 1884, 1995, 2003, 2020]), [1884, 2020])


if __name__ == '__main__':
    main()
