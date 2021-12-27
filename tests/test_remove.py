import unittest

import os
import pathlib
import finder

class TestRemove(unittest.TestCase):
    def test_remove(self):
        path = "test"
        self.assertEqual(os.path.isfile(path), False)
        
        pathlib.Path(path).touch()
        self.assertEqual(os.path.isfile(path), True)
        
        finder.remove(path, False)
        self.assertEqual(os.path.isfile(path), False)
    
    def test_remove_yes(self):
        pass
    
    def test_remove_no(self):
        pass
    
    def test_remove_other(self):
        pass

if __name__ == "__main__":
    unittest.main()