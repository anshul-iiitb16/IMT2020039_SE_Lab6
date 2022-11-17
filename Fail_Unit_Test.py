#!/usr/bin/python3

import unittest
from Sum_Nat_Nums import sum_natnums

class TestCase(unittest.TestCase):
    def testcases_fail(self):

        data_fail = [-2, 5]

        result_fail_1 = sum_natnums(data_fail[0])
        result_fail_2 = sum_natnums(data_fail[1])

        self.assertEqual(result_fail_1, 1)
        self.assertEqual(result_fail_2, 20)


if __name__ == '__main__':
    unittest.main()
