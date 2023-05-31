import unittest
from reservation import Reservation

class ReservationTest(unittest.TestCase):

    def setUp(self):
        preferencesList = [['Concert', 'sport'],
            ['01.01.2024', '02.01.2024', '16.08.2025', '09.02.2026'],
            ['10:00', '11:00', '15:00'],
            ['1', '2'],
            ['10', '100']]
                
        self.module_instance = Reservation(preferencesList)


    def test_checkEvent(self):   
        event1 = ['Concert', 'Miro', 'Pirotska 5', '01.01.2024', '15:00', 55, 3]
        event2 = ['Blabla', 'Miro', 'Pirotska 5', '01.01.2024', '15:00', 55, 3]
        event3 = ['Blabla', 'Miro', 'Pirotska 5', '01.01.2024', '15:00', 555, 3]
        self.assertTrue(self.module_instance.checkEvent(event1))
        self.assertFalse(self.module_instance.checkEvent(event2))
        self.assertFalse(self.module_instance.checkEvent(event3))
        
        
    def test_formattingLocation(self):
        expectedResult = 'pirotska-5'
        rowLocation = 'pirotska 5'
        result = self.module_instance.formattingLocation(rowLocation)
        self.assertEqual(expectedResult, result)
            

if __name__ == '__main__':
    unittest.main()

