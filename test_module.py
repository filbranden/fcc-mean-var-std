import unittest
import mean_var_std


# the test case
class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = mean_var_std.calculate([2, 6, 2, 8, 4, 0, 1, 5, 7])
        expected = {
            "mean": [
                [3.666666666666, 5.0, 3.0],
                [3.333333333333, 4.0, 4.33333333333],
                3.888888888888,
            ],
            "variance": [
                [9.555555555555, 0.666666666666, 8.666666666666],
                [3.555555555555, 10.66666666666, 6.222222222222],
                6.987654320987,
            ],
            "standard deviation": [
                [3.091206165165, 0.816496580927, 2.943920288775],
                [1.885618083164, 3.265986323710, 2.494438257849],
                2.6434171674156,
            ],
            "max": [[8, 6, 7], [6, 8, 7], 8],
            "min": [[1, 4, 0], [2, 0, 1], 0],
            "sum": [[11, 15, 9], [10, 12, 13], 35],
        }
        self.assertAlmostEqual(
            actual,
            expected,
            "Expected different output when calling 'calculate()' with '[2,6,2,8,4,0,1,5,7]'",
        )

    def test_calculate2(self):
        actual = mean_var_std.calculate([9, 1, 5, 3, 3, 3, 2, 9, 0])
        expected = {
            "mean": [
                [4.666666666666, 4.333333333333, 2.666666666666],
                [5.0, 3.0, 3.6666666666666],
                3.8888888888888,
            ],
            "variance": [
                [9.555555555555, 11.55555555555, 4.222222222222],
                [10.66666666666, 0.0, 14.888888888888],
                9.209876543209,
            ],
            "standard deviation": [
                [3.091206165165, 3.39934634239, 2.0548046676563],
                [3.265986323710, 0.0, 3.85861230093],
                3.034777840832,
            ],
            "max": [[9, 9, 5], [9, 3, 9], 9],
            "min": [[2, 1, 0], [1, 3, 0], 0],
            "sum": [[14, 13, 8], [15, 9, 11], 35],
        }
        self.assertAlmostEqual(
            actual,
            expected,
            "Expected different output when calling 'calculate()' with '[9,1,5,3,3,3,2,9,0]'",
        )

    def test_calculate_with_few_digits(self):
        self.assertRaisesRegex(
            ValueError,
            "List must contain nine numbers.",
            mean_var_std.calculate,
            [2, 6, 2, 8, 4, 0, 1],
        )


if __name__ == "__main__":
    unittest.main()
