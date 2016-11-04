# Music Search API

This is the documentation for the music search API. The backed will grab related wikipedia, spotify playlist and twitter for the user

# API reference  

not deployed, this is only like a toy :)  

## Endpoints  

### GET /getArtist

Get information of the specific artist

**Request Parameters:**  

Parameter| Type | Value
--- | --- | ---
`input`| string | the name of the artist, you could do any funky name you like ;)


**Return information:**  


Information| Format | Value
--- | --- | ---
Wikipedia | string | the related Wikipedia, but sometimes the input is not specific enough to identify a single artist, this will return a empty string
Spotify | string | the trending playlist of the artist, with all the songs concatenated in a string, go figure it out!
twitter | string | all the twitter with related information, every line is a new tweet
