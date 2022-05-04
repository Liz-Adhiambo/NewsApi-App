import unittest
from models import news

News=news.News
class NewsTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the News class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_news = News("Steve Peoples","Trump's bid to shape GOP faces test with voters in May races - The Associated Press - en Español","NEW YORK (AP) — Donald Trump  's post-presidency enters a new phase this month as voters across the U.S. begin weighing the candidates he elevated to pursue a vision of a Republican Party steeped in hard-line populism, culture wars and denial of his loss in t…","https://apnews.com/article/2022-midterm-elections-ohio-donald-trump-campaigns-89a597655ab2c39529c8d38e961a4081","https://storage.googleapis.com/afs-prod/media/7e0485b602844e73871c3f25d25dc72d/3000.jpeg","2022-05-02T11:46:05Z", "NEW YORK (AP) Donald Trump s post-presidency enters a new phase this month as voters across the U.S. begin weighing the candidates he elevated to pursue a vision of a Republican Party steeped in hard… [+8114 chars]")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_news,News))


if __name__ == '__main__':
    unittest.main()