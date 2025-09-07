import unittest
import importlib

class TestAssignmentOne(unittest.TestCase):
    def test_01(self):
        self.assertEqual(asgmt.use_abs_function(-2), 2)
        self.assertEqual(asgmt.use_abs_function(-3), 3)
        self.assertEqual(asgmt.use_abs_function(0), 0)
        self.assertEqual(asgmt.use_abs_function(2), 2)
        self.assertEqual(asgmt.use_abs_function(3), 3)
    def test_02(self):
        self.assertEqual(asgmt.use_pow_function(-2, 3), -8)
        self.assertEqual(asgmt.use_pow_function(-3, 2), 9)
        self.assertEqual(asgmt.use_pow_function(0, 2), 0)
        self.assertEqual(asgmt.use_pow_function(2, 3), 8)
        self.assertEqual(asgmt.use_pow_function(3, 2), 9)
    def test_03(self):
        self.assertEqual(asgmt.use_round_function(2.71828, 3), 2.718)
        self.assertEqual(asgmt.use_round_function(2.71828, 4), 2.7183)
        self.assertEqual(asgmt.use_round_function(3.141592, 2), 3.14)
        self.assertEqual(asgmt.use_round_function(3.141592, 5), 3.14159)
    def test_04(self):
        self.assertEqual(asgmt.use_bin_function(0), '0b0')
        self.assertEqual(asgmt.use_bin_function(1), '0b1')
        self.assertEqual(asgmt.use_bin_function(2), '0b10')
        self.assertEqual(asgmt.use_bin_function(3), '0b11')
        self.assertEqual(asgmt.use_bin_function(4), '0b100')
        self.assertEqual(asgmt.use_bin_function(5), '0b101')
    def test_05(self):
        self.assertFalse(asgmt.use_bool_function(0))
        self.assertTrue(asgmt.use_bool_function(1))
        self.assertTrue(asgmt.use_bool_function(2))
        self.assertTrue(asgmt.use_bool_function(3))
        self.assertTrue(asgmt.use_bool_function(4))
        self.assertTrue(asgmt.use_bool_function(-1))
    def test_06(self):
        self.assertEqual(asgmt.use_int_function(2.71828), 2)
        self.assertEqual(asgmt.use_int_function(3.141592), 3)
        self.assertEqual(asgmt.use_int_function(-2.71828), -2)
        self.assertEqual(asgmt.use_int_function(-3.141592), -3)
        self.assertEqual(asgmt.use_int_function(0.01), 0)
        self.assertEqual(asgmt.use_int_function(-0.01), 0)
    def test_07(self):
        self.assertGreaterEqual(asgmt.calculate_bmi(216, 147), 31)
        self.assertGreaterEqual(asgmt.calculate_bmi(206, 113), 26)
        self.assertGreaterEqual(asgmt.calculate_bmi(211, 110), 24)
        self.assertGreaterEqual(asgmt.calculate_bmi(175, 65), 21)
        self.assertGreaterEqual(asgmt.calculate_bmi(180, 70), 21)
        self.assertLessEqual(asgmt.calculate_bmi(216, 147), 33)
        self.assertLessEqual(asgmt.calculate_bmi(206, 113), 28)
        self.assertLessEqual(asgmt.calculate_bmi(211, 110), 26)
        self.assertLessEqual(asgmt.calculate_bmi(175, 65), 23)
        self.assertLessEqual(asgmt.calculate_bmi(180, 70), 23)
    def test_08(self):
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000), "$1,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000), "$1,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(1000000000), "$1,000,000,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(10000), "$10,000")
        self.assertEqual(asgmt.format_integer_with_dollar_sign_and_commas(100000), "$100,000")
    def test_09(self):
        self.assertFalse(asgmt.is_positive(-2))
        self.assertFalse(asgmt.is_positive(-1))
        self.assertFalse(asgmt.is_positive(0))
        self.assertTrue(asgmt.is_positive(1))
        self.assertTrue(asgmt.is_positive(2))
    def test_10(self):
        self.assertFalse(asgmt.is_even(1))
        self.assertFalse(asgmt.is_even(3))
        self.assertFalse(asgmt.is_even(5))
        self.assertTrue(asgmt.is_even(0))
        self.assertTrue(asgmt.is_even(2))

asgmt = importlib.import_module("answers_solved")
suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentOne)
runner = unittest.TextTestRunner(verbosity=2)
test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))