import unittest
import os
from atomdb import AtomDB

class TestAtomDB(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_db.json'
        self.db = AtomDB(self.db_path)

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def test_insert_and_get(self):
        self.db.insert('key1', 'value1')
        self.assertEqual(self.db.get('key1'), 'value1')

    def test_delete(self):
        self.db.insert('key1', 'value1')
        self.db.delete('key1')
        self.assertIsNone(self.db.get('key1'))

if __name__ == '__main__':
    unittest.main()

