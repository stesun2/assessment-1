# Write your unit tests here!
import unittest
from optimal_change import optimal_change
from optimal_change import BILL, COIN

# Test cases all run and pass
# Test suite has sufficient valid test cases for typical inputs (at least 4-5), testing different cases
# Test suite has test cases for edge cases / special cases (single denomination, exact payment, etc...) 

class OptimalChangeTest(unittest.TestCase):
    """Tests for optimal_change.py"""

    def test_simple_change(self):
        self.assertEqual(optimal_change(0, 0), 0)
        self.assertEqual(optimal_change(5, 10), )
    
    def test_insufficient_amount(self):
        self.assertEqual(optimal_change(10, 5), 'Insufficient amount.')

    def test_bill_change(self):
        # self.assertEqual(optimal_change(0, 100), f'{BILL[100]}')
        print(f'1 {BILL[100]}')
        # self.assertEqual(optimal_change(0, 50), 0)
        # self.assertEqual(optimal_change(0, 20), 0)
        # self.assertEqual(optimal_change(0, 10), 0)
        # self.assertEqual(optimal_change(0, 5), 0)
        # self.assertEqual(optimal_change(0, 1), 0)




if __name__ == '__main__':
    unittest.main()