#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.


#This program will direct you to a page that shows you the news 
#for the current day.
import unittest
import string


class News():
    
    @staticmethod
#returns a string that says the current date
    def getNews():
        import httplib
        import json
        import datetime

        date = datetime.datetime.now() #gets the current date
        return str(date)
        #request = httplib.HTTPConnection('google.com', 80)
        #request.connect()
        #request.request(
        #    'GET', '')
        #response = request.getresponse()
        #return json.loads(response.read())


class TestMe(unittest.TestCase):
    
        @staticmethod
        #checks whether date returned is a string
        def test_date():
            date = News.getNews()
            unittest.TestCase.assertEqual(type(News.date), string)
        
