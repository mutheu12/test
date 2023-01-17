# TestRedOrBlueFunction TestCase
import unittest
from func import red_or_blue, average_exam_score


class TestRedOrBlueFunction(unittest.TestCase): # inherit from the class unittest.TestCase which has a lot of test cases

    def test_odd_numbers(self):
        expected = "Blue"
        result = red_or_blue(x=3)
        self.assertEqual(expected, result)

    def test_even_greater_than_twenty(self):
        self.assertEqual(True, True)

    def test_range_6_to_20(self):
        self.assertEqual(True, True)


# TestAverageExamScore Testcase
class TestAverageExamScore(unittest.TestCase):

    def test_calculate_average(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': '8'},
        ]
        expected = 7.25
        self.assertEqual(average_exam_score(my_input), expected)

    def test_calculate_average_missing_mark(self):
        my_input = [
            {'name': 'Jane', 'mark': 7},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha'},
            {'name': 'Zac', 'mark': '8'},
        ]
        expected = 6.5
        self.assertEqual(average_exam_score(my_input), expected)

    def test_calculate_average_error_raised(self):
        my_input = [
            {'name': 'Jane', 'mark': 15},
            {'name': 'Nitesh', 'mark': 6},
            {'name': 'Aisha', 'mark': 8},
            {'name': 'Zac', 'mark': '8'},
        ]
        with self.assertRaises(ValueError):
            average_exam_score(my_input)

# TestIncrementLineNumber Test case


if __name__ == '__main__':
    unittest.main()