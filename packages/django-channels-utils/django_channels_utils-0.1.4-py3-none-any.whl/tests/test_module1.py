import unittest
from django_channels_utils import hello_world


class TestModule1(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(hello_world(), "Hello World!" )
        
if __name__=="__main__":
    unittest.main()