import unittest
from src.service import Service

class TestService(unittest.TestCase):
    def setUp(self):
        self.service = Service("Layanan A", 5)
    
    def test_service_name(self):
        self.assertEqual(self.service.name, "Layanan A")
    
    def test_max_capacity(self):
        self.assertEqual(self.service.max_capacity, 5)
    
    def test_update_capacity(self):
        self.service.set_capacity(10)
        self.assertEqual(self.service.max_capacity, 10)

if __name__ == "__main__":
    unittest.main()