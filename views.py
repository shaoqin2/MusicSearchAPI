from flask import Flask, request
from app import app
import urllib2
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
@app.route('/artistEndpoint', methods=['GET'])
def artistEndpoint():
	if 'artist' in request.args:
   		artistResponse = urllib2.urlopen("https://api.spotify.com/v1/search?q=" + request.args["artist"]+ "&type=artist").read()
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

