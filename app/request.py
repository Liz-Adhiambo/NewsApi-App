from app import app
import urllib.request,json
from .models import news

News = news.News

# Getting api key
api_key = app.config['NEWS_API_KEY']

# Getting the movie base url
base_url = app.config['NEWS_BASE_URL']


def get_news():
    get_news_url= base_url.format(api_key)
    
    with urllib.request.urlopen(get_news_url)as url:
        get_news_data=url.read()
        get_news_response=json.loads(get_news_data)
        
        news_results=None
        
        if get_news_response['articles']:
         news_results_list=get_news_response['articles']
         news_results=process_results(news_results_list)
    return news_results

def process_results(news_list):
    news_results=[]
    for news_result in news_list:
        author=news_result.get('author')
        title=news_result.get('title')
        description=news_result.get('description')
        url=news_result.get('url')
        urlToImage=news_result.get('urlToImage')
        publishedAt=news_result.get('publishedAt')
        content=news_result.get('content')
        
        news_object=News(author,title,description,url,urlToImage,publishedAt,content)
        news_results.append(news_object)
        
    return news_results
