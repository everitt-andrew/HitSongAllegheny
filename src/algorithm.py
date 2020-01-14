#import statements
import csv
from sklearn.neural_networkimport MLPClassifier
import matplotlib

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

#neural network settings
solver='adam'
