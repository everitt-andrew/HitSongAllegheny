#import statements
import csv
from sklearn.neural_networkimport MLPClassifier
import matplotlib
import sys

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
variables = ["Artist popularity", "Genre", "Length", "Loudness", "Tempo", "Key"]
clf = MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(5, 2), random_state=1)

#algorithm training
X = [[0., 0.], [1., 1.]]
y = [0, 1]
clf.fit(X, y)

#prediction algorithm
clf.predict([[2., 2.], [-1., -2.]])
array([1, 0])

#output
plt.show()
