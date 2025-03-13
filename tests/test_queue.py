import unittest
from src.queue import QueueSystem # type: ignore

class TestQueueSystem(unittest.TestCase):
    def setUp(self):
        self.queue = QueueSystem()
    
    def test_add_to_queue(self):
        self.queue.add_to_queue("User1", "Layanan A")
        self.assertEqual(len(self.queue.queue), 1)
    
    def test_process_queue(self):
        self.queue.add_to_queue("User1", "Layanan A")
        self.queue.process_next()
        self.assertEqual(len(self.queue.queue), 0)
    
    def test_queue_status(self):
        self.queue.add_to_queue("User1", "Layanan A")
        self.assertEqual(self.queue.get_queue_status(), [("User1", "Layanan A")])

if __name__ == "__main__":
    unittest.main()