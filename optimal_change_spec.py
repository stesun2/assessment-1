# Write your unit tests here!
import unittest
from optimal_change import optimal_change

class OptimalChangeTest(unittest.TestCase):
    """Tests for optimal_change.py"""

    def test_simple_change(self):
        self.assertEqual(optimal_change(0,0), 0)




if __name__ == '__main__':
    unittest.main()