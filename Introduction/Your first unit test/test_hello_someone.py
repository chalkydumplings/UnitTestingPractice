import unittest

from hello_someone import hello_someone

# you have to import unit test. TestCase for some reason not sure exactly why
class TestHelloWorld(unittest.TestCase):

    def test_hello_world(self):

        self.assertEqual(hello_someone("julie"), "Hello, julie!")
