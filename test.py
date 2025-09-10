<<<<<<< HEAD
import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Tannu"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "Tannu")  

if __name__ == '__main__':
    unittest.main()
=======
import unittest
from main import to_upper

class MyTestCase(unittest.TestCase):
    def test_to_upper(self):
        name = "Tannu"
        upper_name = to_upper(name)
        self.assertEqual(upper_name, "TANNU")  

if __name__ == '__main__':
    unittest.main()
>>>>>>> 1d03134ac0c7e8f955cbffe1e4e0b3c417f4b65b
