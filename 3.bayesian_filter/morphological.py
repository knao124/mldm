import urllib
import urllib2
from bs4 import BeautifulSoup
appid = 'dj0zaiZpPUNlNmFsN1Q5MFZOeSZzPWNvbnN1bWVyc2VjcmV0Jng9ZTc-' 
pageurl = "http://jlp.yahooapis.jp/MAService/V1/parse"

def split(sentence, appid=appid, results="ma", filter="1|2|3|4|5|9|10"):
    sentence = sentence.encode("utf-8")
    params = urllib.urlencode({'appid':appid, 'results':results, 'filter':filter, 'sentence':sentence})
    results = urllib2.urlopen(pageurl, params)
    soup = BeautifulSoup(results.read())
    return [w.surface.string for w in soup.ma_result.word_list]
