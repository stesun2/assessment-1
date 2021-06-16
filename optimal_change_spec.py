# Write your unit tests here!
import unittest
from optimal_change import optimal_change

# Test cases all run and pass
# Test suite has sufficient valid test cases for typical inputs (at least 4-5), testing different cases
# Test suite has test cases for edge cases / special cases (single denomination, exact payment, etc...) 

class OptimalChangeTest(unittest.TestCase):
    """Tests for optimal_change.py"""
    
    def test_insufficient_amount(self):
        self.assertEqual(optimal_change(10, 5), 'Insufficient amount.')
        self.assertEqual(optimal_change(20, 1), 'Insufficient amount.')

    def test_bill_change(self):
        self.assertEqual(optimal_change(0, 100), 'The optimal change for an item that costs $0.00 with an amount paid of $100 is 1 $100 bill, ')
        self.assertEqual(optimal_change(0, 50), 'The optimal change for an item that costs $0.00 with an amount paid of $50 is 1 $50 bill, ')
        self.assertEqual(optimal_change(0, 20), 'The optimal change for an item that costs $0.00 with an amount paid of $20 is 1 $20 bill, ')
        self.assertEqual(optimal_change(0, 10), 'The optimal change for an item that costs $0.00 with an amount paid of $10 is 1 $10 bill, ')
        self.assertEqual(optimal_change(0, 5), 'The optimal change for an item that costs $0.00 with an amount paid of $5 is 1 $5 bill, ')
        self.assertEqual(optimal_change(0, 1), 'The optimal change for an item that costs $0.00 with an amount paid of $1 is 1 $1 bill, ')

    def test_coin_change(self):
        self.assertEqual(optimal_change(0, 0.25), 'The optimal change for an item that costs $0.00 with an amount paid of $0.25 is 1 quarter, ')
        self.assertEqual(optimal_change(0, 0.10), 'The optimal change for an item that costs $0.00 with an amount paid of $0.1 is 1 dime, ')
        self.assertEqual(optimal_change(0, 0.05), 'The optimal change for an item that costs $0.00 with an amount paid of $0.05 is 1 nickel, ')
        self.assertEqual(optimal_change(0, 0.01), 'The optimal change for an item that costs $0.00 with an amount paid of $0.01 is and 1 penny. ')
    
    def test_hard_change(self):
        self.assertEqual(optimal_change(10, 10), 'The optimal change for an item that costs $10.00 with an amount paid of $10 is no change.')
        self.assertEqual(optimal_change(10, 11.25), 'The optimal change for an item that costs $10.00 with an amount paid of $11.25 is 1 $1 bill, 1 quarter, ')
        self.assertEqual(optimal_change(10, 11.24), 'The optimal change for an item that costs $10.00 with an amount paid of $11.24 is 1 $1 bill, 2 dimes, and 4 pennies.')
        self.assertEqual(optimal_change(10, 11.23), 'The optimal change for an item that costs $10.00 with an amount paid of $11.23 is 1 $1 bill, 2 dimes, and 3 pennies.')
        self.assertEqual(optimal_change(10, 11.18), 'The optimal change for an item that costs $10.00 with an amount paid of $11.18 is 1 $1 bill, 1 dime, 1 nickel, and 3 pennies.')      
        self.assertEqual(optimal_change(10, 11.50), 'The optimal change for an item that costs $10.00 with an amount paid of $11.5 is 2 $1 bills, ')

    def test_harder_change(self):
        self.assertEqual(optimal_change(62.13, 100), 'The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 3 $1 bills, ')
        self.assertEqual(optimal_change(31.51, 50), 'The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.')
        self.assertEqual(optimal_change(1.99, 100), 'The optimal change for an item that costs $1.99 with an amount paid of $100 is 1 $50 bill, 2 $20 bills, 1 $5 bill, 3 $1 bills, and 1 penny. ')
        self.assertEqual(optimal_change(1.49, 200), 'The optimal change for an item that costs $1.49 with an amount paid of $200 is 1 $100 bill, 1 $50 bill, 2 $20 bills, 1 $5 bill, 4 $1 bills, ')
        self.assertEqual(optimal_change(1.71, 300), 'The optimal change for an item that costs $1.71 with an amount paid of $300 is 2 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, 3 $1 bills, 1 quarter, and 4 pennies.')
        self.assertEqual(optimal_change(1.25, 400), 'The optimal change for an item that costs $1.25 with an amount paid of $400 is 3 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, 4 $1 bills, ')
        self.assertEqual(optimal_change(1.12, 500), 'The optimal change for an item that costs $1.12 with an amount paid of $500 is 4 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, 4 $1 bills, ')
        self.assertEqual(optimal_change(1.13, 600), 'The optimal change for an item that costs $1.13 with an amount paid of $600 is 5 $100 bills, 1 $50 bill, 2 $20 bills, 1 $5 bill, 4 $1 bills, ')

if __name__ == '__main__':
    unittest.main()