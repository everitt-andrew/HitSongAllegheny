#import statements
import csv
import spotipy
import json

file = "../data/musiclist.csv"

#reading the csv file
with open(file, 'rb') as f:
    reader = csv.reader(f)
    try:
        #testing csv is read correctly
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (file, reader.line_num, e))


#writing to setup csv file
with open(file, 'w') as csvfile:
    fieldnames = ['week', 'position', 'title', 'artist', 'features', 'url', 'release_date', 'date_difference', 'length', 'explicit', 'loudness', 'l_confidence', 'tempo', 't_confidence', 'key', 'k_confidence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

#connecting to the spotify web API and retrieving data
spotify = spotipy.Spotify()

#parse each song (row) for url
for(int i = 0; i < rows; i++){
    id = reader['url']
    #begin to retrive nine other variables
    data = spotify.audio_analysis(id)

    #writes terminal output to json file
    with open('data.json', 'w') as f:
        json.dump(data, f)

    #parsing through each variable in json file

    #length
    row[6] =

    #explicit
    row[7] =

    #loudness
    row[8] =

    #loudness confidence
    row[9] =

    #tempo
    row[10] =

    #tempo confidence
    row[11] =

    #key
    row[12] =

    #key confidence
    row[13] =

    #writing all results to csv file
    writer.writerow(row)

}


#testing csv is updated correctly
with open(file, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
