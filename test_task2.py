import unittest
from task2 import MathEquatations

class TestMathEquatations(unittest.TestCase):

    def test_operation_with_arithmetic_sequence(self):
        self.assertEqual(MathEquatations.operation_with_arithmetic_sequence([1,2,3,4,5,6]),0.1707825127659933)

    def test_operation_with_arithmetic_sequence_1(self):
        self.assertEqual(MathEquatations.operation_with_arithmetic_sequence([1,2,3,4,5]),0.3535533905932738)

    def test_operation_with_arithmetic_sequence_2(self):
        self.assertEqual(MathEquatations.operation_with_arithmetic_sequence([1,2,3,4]),0.6454972243679028)

    def test_operation_with_arithmetic_sequence_3(self):
        self.assertEqual(MathEquatations.operation_with_arithmetic_sequence([1,2,3]),1)

    def test_equatations_with_median(self):
        self.assertEqual(MathEquatations.equatations_with_median([1,2,3,4,5,6]),5.497787143782138)

    def test_equatations_with_median_1(self):
        self.assertEqual(MathEquatations.equatations_with_median([1,2,3,4,5]),4.71238898038469)

    def test_equatations_with_median_2(self):
        self.assertEqual(MathEquatations.equatations_with_median([1,2,3,4]),3.9269908169872414)

    def test_equatations_with_median_3(self):
        self.assertEqual(MathEquatations.equatations_with_median([1,2,3]),3.141592653589793)


