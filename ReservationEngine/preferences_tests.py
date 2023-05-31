import unittest
from preferences import Preferences

class PrefsTest(unittest.TestCase):

    def setUp(self):
        self.module_instance = Preferences("userPref.txt")

    def test_createUserPreferencesList(self):   
        expected_output = [
            ['Concert', 'sport'],
            ['01.01.2024', '02.01.2024', '16.08.2025', '09.02.2026'],
            ['10:00', '11:00', '15:00'],
            ['1', '2'],
            ['10', '100'],
        ]
        
        result = self.module_instance.createUserPreferencesList()

        self.assertEqual(result, expected_output)
        
        
if __name__ == '__main__':
    unittest.main()

