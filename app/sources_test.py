import unittest
from models import news

Sources=news.Sources
class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_Sources = Sources()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_Sources,Sources))


if __name__ == '__main__':
    unittest.main()