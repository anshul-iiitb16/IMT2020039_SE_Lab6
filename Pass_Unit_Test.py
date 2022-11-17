#!/usr/bin/python3

import unittest
from Sum_Nat_Nums import sum_natnums

class TestCase(unittest.TestCase):
    def testcases_pass(self):

        data_pass = [1, 5, 10]

        result_pass_1 = sum_natnums(data_pass[0])
        result_pass_2 = sum_natnums(data_pass[1])
        result_pass_3 = sum_natnums(data_pass[2])

        self.assertEqual(result_pass_1, 1)
        self.assertEqual(result_pass_2, 15)
        self.assertEqual(result_pass_3, 55)


if __name__ == '__main__':
    unittest.main()
