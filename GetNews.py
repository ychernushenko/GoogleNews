class News():
    
    @staticmethod
    def getNews():
        import httplib
        import json
        import datetime

        date = datetime.datetime.now()
        request = httplib.HTTPConnection('google.com', 80)
        request.connect()
        request.request(
            'GET', '/#q=news+/' + str(date))
        response = request.getresponse()
        return json.loads(response.read())