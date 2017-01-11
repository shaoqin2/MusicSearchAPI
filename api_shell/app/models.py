import json
import os
import base64
import urllib2,urllib
class twitter:
    """the twitter API wrapper to grab relavent tweets"""

    token = ""
    def __init__(self):
        APP_ROOT = os.path.dirname(os.path.abspath(__file__))
        #APP_STATIC = os.path.join(APP_ROOT, 'static')
        keystr = open(os.path.join(APP_ROOT, 'secret.txt'),'r').read()
        keydict = json.loads(keystr)
    	consumerKey = keydict["consumerKey"]
    	consumerSecret = keydict["consumerSecret"]
    	keySecret = consumerKey+":"+consumerSecret
    	encoded = base64.b64encode(keySecret)
    	authUrl = 'https://api.twitter.com/oauth2/token'
    	headers = {'Authorization':'Basic ' + encoded, 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
    	values = {'grant_type':'client_credentials'}
    	data = urllib.urlencode(values)
    	authRequest = urllib2.Request(authUrl,data,headers)
    	authResponse = urllib2.urlopen(authRequest).read()
    	authJson = json.loads(authResponse)
    	self.token = authJson['access_token']

    def getTweets(self,input):


    	url = "https://api.twitter.com/1.1/search/tweets.json?q="+input;
    	#headers = {'Authorization':'Bearer '+token}
    	searchRequest = urllib2.Request(url)
    	searchRequest.add_header('Authorization', 'Bearer '+self.token)
    	response = urllib2.urlopen(searchRequest).read()
    	jsonObject = json.loads(response)
    	try:
    		printJob=""
    		for status in jsonObject['statuses']:
    			printJob = printJob + status["text"].encode('utf-8') + '<br/>'
    		return str(input)+"</br>"+str(printJob)
    	except ValueError as a:
    		return "Your request hit the following error:<br/>"+ str(a)
    	return "Bad request"

class spotify:
    '''the spotify wrapper to grab artist songs and albums'''
    def __init__(self):
        pass
    def getPlaylist(self,input):
     	artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=" + input+ "&type=artist").read()
    	artistJson = json.loads(artistResponse)
    	id = str(artistJson['artists']['items'][0]["id"])
    	topAlbumResponse = urllib2.urlopen("https://api.spotify.com/v1/artists/"+id+"/top-tracks?country=US").read()
    	tracks = json.loads(topAlbumResponse)['tracks']
    	string = ""
    	for i in xrange(len(tracks)):
    		string += tracks[i]["name"] + ", "
    	return string

    	albums = []
    	for album in albumIn:
    		albums.append(album['name'])
    	string = ""
    	for i in xrange(len(albums)):
    		string += albums[i] +", "
    	return string

class wiki:
    '''wiki wrapper to grab wiki'''
    def __init__(self):
        pass
    def getWiki(self,input):
    	url = "https://en.wikipedia.org/w/api.php?action=opensearch&search=" + input + "&limit=1&namespace=0&format=json"
    	searchRequest = urllib2.Request(url)
    	response = urllib2.urlopen(searchRequest).read()
    	wikiJson = json.loads(response)
    	#for key in wikiJson["query"]["pages"]:
    	try:
    		return wikiJson[2][0]
    		#return wikiJson["query"]#["pages"][key]#["extract"]
    	except Exception as e:
    		return str(e)
