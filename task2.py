import math
import statistics
import sys

class MathEquatations:


    
    def count_product_of_list(sequence:list) -> float:
        a = 1
        for i in sequence:
            a *= i
        return a

    @staticmethod
    # computes the square root of the sum of a sequence of numbers given as an argument, divided by the product of the sequence
    def operation_with_arithmetic_sequence(sequence:list) -> float:
        return math.sqrt(sum(sequence)/MathEquatations.count_product_of_list(sequence))

    @staticmethod
    # determines the median of numbers, multiplied by half of PI and finally increased by the Epsilon constant
    def equatations_with_median(sequence:list) -> float:
        return statistics.median(sequence)*(math.pi/2) + sys.float_info.epsilon





