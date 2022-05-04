from app import app
import urllib.request,json
from .models import news



sources=news.Sources

apikey = '77778d372be048dc9186f0621247ab9f'
baseurl = 'https://newsapi.org/v2/top-headlines/sources?apiKey={}'
def get_sources():
    get_sources_url= baseurl.format(apikey)
    
    with urllib.request.urlopen(get_sources_url)as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)
        
        sources_results=None
        
        if get_sources_response['sources']:
         sources_results_list=get_sources_response['sources']
         sources_results=process_results(sources_results_list)
    return sources_results

def process_results(sources_list):
    sources_results=[]
    for sources_result in sources_list:
        id=sources_result.get('id')
        name=sources_result.get('name')
        description=sources_result.get('description')
        url=sources_result.get('url')
        category=sources_result.get('category')
        country=sources_result.get('country')
        
        
        sources_object=sources(id,name,description,url,category,country)
        sources_results.append(sources_object)
        
    return sources_results



