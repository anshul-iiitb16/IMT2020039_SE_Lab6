#!/usr/bin/python3

import unittest
from Sum_Nat_Nums import sum_natnums

class TestCase(unittest.TestCase):
    def testcases_fail_1(self):

        data_fail = [-2]
        result_fail_1 = sum_natnums(data_fail[0])
        self.assertEqual(result_fail_1, 1)

    def testcases_fail_2(self):

        data_fail = [5]
        result_fail_2 = sum_natnums(data_fail[0])
        self.assertEqual(result_fail_2, 500)


if __name__ == '__main__':
    unittest.main()