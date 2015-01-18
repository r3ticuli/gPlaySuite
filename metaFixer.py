import gmusicapi

api = gmusicapi.Mobileclient()
badTitle = []
badArtist = []
badAlbum = []
badKey = []

if api.login('c0taxt','pingapie666!') :
    songs = api.get_all_songs()
    for song in songs :
        try :
            if song['album'].replace(" ", "") == "" :
                badAlbum.append(song)
            if song['artist'].replace(" ", "") == "" :
                badArtist.append(song)
            if song['title'].replace(" ", "") == "" :
                badTitle.append(song)
        except KeyError, e:
            song["errorId"] = e
            badKey.append(song)

            
    print ("bad title : " + str (len(badTitle)))

    print ("bad arist : " + str(len(badArtist)))

    print ("bad album : " + str(len(badAlbum)))
    
    print ("bad keys : " + str(len(badKey)))

else :
    print('login failed!')

