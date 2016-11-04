from flask import Flask, request
from . import models
import urllib2, urllib
from app import app
import base64
import json

# static url
@app.route('/')
def index():
    return "Hello, World!"

twitter = models.twitter()
spotify = models.spotify()
wiki = models.wiki()

@app.route('/getArtist')
def getArtist():
	if 'input' in request.args:
		input = request.args['input']
		return str(wiki.getWiki(input)) + "<br><br>" + str(spotify.getPlaylist(input))+ "<br><br>" +str(twitter.getTweets(input))
	else:
		return "Bad request"
