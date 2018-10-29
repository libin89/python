# test unit
import unittest
from function import get_formatted_name

# unittest Module assert functions
# assertEqual(a, b)   check a == b
# assertNotEqual(a, b) check a != b
# assertTrue(x)  check x is True
# assertFalse(x)  check x is False
# assertIn(item, list)  check item in list
# assertNotIn(item, list)  check item not in list

# setUp() will be called first if exist.
# functions prefix of TestCase must be test_

class NamesTestCase(unittest.TestCase):
    """test function.py"""
    def setUp(self):
        """first call"""
        pass
    def test_first_last_name(self):
        formatted_name = get_formatted_name(
            'janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()
