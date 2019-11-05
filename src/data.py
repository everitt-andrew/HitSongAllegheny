#import statements
import csv
#import spotipy

file = "../data/musiclist.csv"
with open(file, 'w') as csvfile:
    fieldnames = ['week', 'position', 'title', 'artist', 'features', 'url', 'genre', 'length', 'explicit', 'loudness', 'l_confidence', 'tempo', 't_confidence', 'key', 'k_confidence']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
with open(file, 'rb') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            #retrieve spotify data
    except csv.Error as e:
        sys.exit('file %s, line %d: %s' % (filename, reader.line_num, e))
