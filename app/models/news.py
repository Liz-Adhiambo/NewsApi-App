class News:
    def __init__(self,author,title,description,url,urlToImage,publishedAt,content):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        self.content = content
        
        
class Sources:
    '''
    Class to return sources from newsAPI
    '''
    def __init__(self,id,name,description,url,category,country):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category
        self.country=country
        
class Everything:
    '''
    Defining everything object that with pull based on category
    '''
    def __init__(self,author,title,description,url,urlToImage,publishedAt):
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt
        