from flask import Flask, request
import urllib2, urllib
from app import app
import base64
import json

# static url
@app.route('/')
def index():
    return "Hello, World!"

# url parameters
@app.route('/endpoint/<input>')
def endpoint(input):
    return input

# api with endpoint
@app.route('/nameEndpoint', methods=['GET'])
def nameEndpoint():
    if 'name' in request.args:
    	return 'My name is ' + request.args['name']

@app.route('/getArtist')
def getArtist():
	if 'input' in request.args:
		input = request.args['input']
		return str(wiki(input)) + "<br><br>" + str(spotify(input))+ "<br><br>" +str(twitter(input))
	else:
		return "Bad request"

def wiki(input):
	url = "https://en.wikipedia.org/w/api.php?format=json&action=query&prop=extracts&exintro=&explaintext=&titles="+input
	searchRequest = urllib2.Request(url)
	response = urllib2.urlopen(searchRequest).read()
	wikiJson = json.loads(response)
	for key in wikiJson["query"]["pages"]:
		return wikiJson["query"]["pages"][key]["extract"]


def spotify(input):
 	artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=" + input+ "&type=artist").read()
	artistJson = json.loads(artistResponse)
	id = str(artistJson['artists']['items'][0]["id"])
	topAlbumResponse = urllib2.urlopen("https://api.spotify.com/v1/artists/"+ id+ "/albums").read()
	#return str(json.loads(topAlbumResponse)['items'][0]['name'])
	albums = []
	for album in json.loads(topAlbumResponse)['items']:
		albums.append(album['name'])
	string = "" 
	for title in albums:
		string += title +", "
		return string

def twitter(input):
	consumerKey = "P66GTF3aYSQQYdQRg56N3H9Ms"
	consumerSecret = "TSiTIh64f8XVcS1WoE59uZ3dTvQ2qkaPnTjQwIfW6IwrnybOmg"
	keySecret = consumerKey+":"+consumerSecret
	encoded = base64.b64encode(keySecret)
	authUrl = 'https://api.twitter.com/oauth2/token'
	headers = {'Authorization':'Basic ' + encoded, 'Content-Type':'application/x-www-form-urlencoded;charset=UTF-8'}
	values = {'grant_type':'client_credentials'}
	data = urllib.urlencode(values)
	authRequest = urllib2.Request(authUrl,data,headers)
	authResponse = urllib2.urlopen(authRequest).read()
	authJson = json.loads(authResponse)
	token = authJson['access_token']

	url = "https://api.twitter.com/1.1/search/tweets.json?q="+input;
	#headers = {'Authorization':'Bearer '+token}
	searchRequest = urllib2.Request(url)
	searchRequest.add_header('Authorization', 'Bearer '+token)
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

