import unittest
from database_connecting import DatabaseConnector

class dbConnectorTests(unittest.TestCase):

    def setUp(self):
        self.module_instance = DatabaseConnector("eventDatabase.db")

    def test_openDataBase(self):   
        self.assertFalse(self.module_instance.openDataBase() == 'None');
        
    def test_getEventList(self):
        
        expected_output = [
            ('Concert', 'Miro', 'Pirotska 5', '01.01.2024', '15:00', 55, 3),
            ('Concert', 'Miro', 'Pirotska 5', '02.01.2024', '15:00', 65, 4)]
        
        result = self.module_instance.getEventList()

        self.assertEqual(result, expected_output)
    
    def test_getNumberOfEvents(self):
        self.assertEqual(self.module_instance.getNumberOfEvents() , 2);    
    
if __name__ == '__main__':
    unittest.main()

