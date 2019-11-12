#import statements
import csv
import spotipy

file = "../data/musiclist.csv"

#reading the csv file
with open(file, 'rb') as f:
    reader = csv.reader(f)
    try:
        #testing csv is read correctly
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))


#writing to setup csv file
with open(file, 'w') as csvfile:
    fieldnames = ['week', 'position', 'title', 'artist', 'features', 'url', 'genre', 'length', 'explicit', 'loudness', 'l_confidence', 'tempo', 't_confidence', 'key', 'k_confidence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#connecting to the spotify web API and retrieving data
spotify = spotipy.Spotify()

#parse each row for url
for(int i = 0; i < rows; i++){
    id = reader['url']

    #retrive nine other parameters
    results = spotify.audio_analysis(id);

    #writing results to csv file
    

}


#testing csv is updated correctly
with open(file, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
