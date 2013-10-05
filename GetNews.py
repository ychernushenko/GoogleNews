class News():
    
    @staticmethod
    def getNews():
        import httplib
        import json
        import datetime

        date = datetime.datetime.now()
        request = httplib.HTTPConnection('news.google.com', 80)
        request.connect()
        request.request('GET', '/')
        response = request.getresponse()
        return response.read()
