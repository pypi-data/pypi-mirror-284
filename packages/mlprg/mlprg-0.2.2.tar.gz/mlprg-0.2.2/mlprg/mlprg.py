def prg1():
   code = """
import csv
def loadcsv(filename):
  lines=csv.reader(open(filename,"r"))
  dataset = list(lines)
  headers=dataset.pop(0)
  return dataset,headers
def print_hypoyhesis(h):
  print('<',end='')
  for i in range(0,len(h)-1):
    print(h[i],end=',')
  print('>')
def findS():
  dataset,features=loadcsv("/sports1.csv")
  rows=len(dataset)
  cols=len(dataset[0])
  flag=0
  for x in range(0,rows):
    t=dataset[x]
    if t[-1]=='1' and flag==0:
      flag=1
      h=dataset[x]
    elif t[-1] == '1':
      for y in range(cols):
        if h[y]!=t[y]:
          h[y]='?'
  print("The maximally specific hypothessis for a given trainsing exams")
  print_hypoyhesis(h)
findS()
        """
   print(code)
def prg2():

   code="""
import numpy as np
import pandas as pd

df = pd.read_csv("sports1.csv")
concept=np.array(df.iloc[:,0:-1])
target=np.array(df.iloc[:,-1])

def learn(concept,target):
    specific_h=concept[0].copy()
    print("Most specific",specific_h)
    general_h=[["?" for i in range(len(specific_h))] for i in range(len(specific_h))]
    print("General",general_h)

    for i,h in enumerate(concept):
        print("Instances", i+1, "is", h)
        if target[i]==1:
            print("Instance is positive")
            for x in range(len(specific_h)):
                if(h[x]!=specific_h[x]):
                    specific_h[x]='?'
                    general_h[x][x]='?'

        if(target[i]==0):
            print("instance is negative")
            for x in range(len(specific_h)):
                if h[x]!=specific_h[x]:
                    general_h[x][x]=specific_h[x]
                else:
                    general_h[x][x]='?'
        print("Specific boundary", i+1, specific_h)
        print("General bundary", i+1, general_h)
        print("\n")

learn(concept, target)
"""
   print(rf'{code}')
def prg3():
   code = """
   
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from sklearn import tree

df=pd.read_csv("Iris.csv")
df.head()

df.drop('Id',axis=1,inplace=True)
df.head()

le = LabelEncoder()
df['Species']= le.fit_transform(df['Species'])
df['Species'].unique()

X=df.iloc[:,:4]
y=df.iloc[:,4:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=123)

clf=DecisionTreeClassifier(criterion='entropy', splitter='best', max_leaf_nodes=3)
clf.fit(X_train,y_train.values.ravel())
y_pred=clf.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

confusion_matrix(y_test, y_pred)

fn=['SepalLengthCm'	,'SepalWidthCm'	,'PetalLengthCm',	'PetalWidthCm']#column names of the dataset
cn=['Iris-setosa','	Iris-versicolor','Iris-virginica']#names of classes to be classified

fig, axes = plt.subplots(nrows = 1,ncols = 1,figsize = (2,2), dpi=200)
tree.plot_tree(clf,
               feature_names = fn,
               class_names=cn,
               filled = True);

species_check = clf.predict([[4.7,	3.2,	1.3,	0.2]])[0]
   """
   print(code)

def prg4():
   code="""
import numpy as np

X = np.array(([2, 9], [1, 5], [3, 6]), dtype=float)
y = np.array(([92], [86], [89]), dtype=float)

X = X / np.amax(X, axis=0)
y = y / 100

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def derivatives_sigmoid(x):
    return x * (1 - x)

epoch = 5000
lr = 0.1
inputlayer_neurons = 2
hiddenlayer_neurons = 3
output_neurons = 1

wh = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
bh = np.random.uniform(size=(1, hiddenlayer_neurons))
wout = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for i in range(epoch):
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)
    outinp1 = np.dot(hlayer_act, wout)
    outinp = outinp1 + bout
    output = sigmoid(outinp)

    EO = y - output
    outgrad = derivatives_sigmoid(output)
    d_output = EO * outgrad
    EH = d_output.dot(wout.T)

    hiddengrad = derivatives_sigmoid(hlayer_act)
    d_hiddenlayer = EH * hiddengrad

    wout += hlayer_act.T.dot(d_output) * lr
    bout += np.sum(d_output, axis=0, keepdims=True) * lr
    wh += X.T.dot(d_hiddenlayer) * lr
    bh += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr

print(r"Input: \n" + str(X))
print(r"Actual Output: \n" + str(y))
print(r"Predicted Output: \n" + str(output))
   
   """
   print(rf'{code}')
def prg5():
   code = """ 
import csv, random, math
import statistics as st

def loadCsv(filename):
    lines = csv.reader(open(filename, "r"));
    dataset = list(lines)
    for i in range(len(dataset)):
        dataset[i] = [float(x) for x in dataset[i]]
    return dataset

def splitDataset(dataset, splitRatio):
    testSize = int(len(dataset) * splitRatio);
    trainSet = list(dataset);
    testSet = []
    while len(testSet) < testSize:
        index = random.randrange(len(trainSet));
        testSet.append(trainSet.pop(index))
    return [trainSet, testSet]
def separateByClass(dataset):
    separated = {}
    for i in range(len(dataset)):
        x = dataset[i]
        if (x[-1] not in separated):
            separated[x[-1]] = []
        separated[x[-1]].append(x)
    return separated
def compute_mean_std(dataset):
    mean_std = [ (st.mean(attribute), st.stdev(attribute))
                for attribute in zip(*dataset)];
    del mean_std[-1]
    return mean_std
def summarizeByClass(dataset):
    separated = separateByClass(dataset);
    summary = {}
    for classValue, instances in separated.items():
        summary[classValue] = compute_mean_std(instances)
    return summary
def estimateProbability(x, mean, stdev):
    exponent = math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1 / (math.sqrt(2*math.pi) * stdev)) * exponent
def calculateClassProbabilities(summaries, testVector):
    p = {}
    for classValue, classSummaries in summaries.items():
        p[classValue] = 1
        for i in range(len(classSummaries)):
            mean, stdev = classSummaries[i]
            x = testVector[i]
            p[classValue] *= estimateProbability(x, mean, stdev);
    return p
def predict(summaries, testVector):
    all_p = calculateClassProbabilities(summaries, testVector)
    bestLabel, bestProb = None, -1
    for lbl, p in all_p.items():
        if bestLabel is None or p > bestProb:
            bestProb = p
            bestLabel = lbl
    return bestLabel
def perform_classification(summaries, testSet):
    predictions = []
    for i in range(len(testSet)):
        result = predict(summaries, testSet[i])
        predictions.append(result)
    return predictions
def getAccuracy(testSet, predictions):
    correct = 0
    for i in range(len(testSet)):
        if testSet[i][-1] == predictions[i]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0
dataset = loadCsv('naivebasedataset.csv');
print('Pima Indian Diabetes Dataset loaded...')
print('Total instances available :',len(dataset))
print('Total attributes present :',len(dataset[0])-1)
print("First Five instances of dataset:")
for i in range(5):
    print(i+1 , ':' , dataset[i])
splitRatio = 0.2
trainingSet, testSet = splitDataset(dataset, splitRatio)
print('\nDataset is split into training and testing set.')
print('Training examples = {0} \nTesting examples = {1}'.format(len(trainingSet),
len(testSet)))
summaries = summarizeByClass(trainingSet)
predictions = perform_classification(summaries, testSet)
accuracy = getAccuracy(testSet, predictions)
print('\nAccuracy of the Naive Baysian Classifier is :', accuracy)
   """
   print(rf'{code}')
def prg6():
   code = """
import matplotlib.pyplot as plt
from sklearn.inspection import DecisionBoundaryDisplay
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pandas as pd

df = pd.read_csv("Iris.csv")
df.drop('Id',axis=1,inplace=True)
df.head()

df.info()

le = LabelEncoder()
df['Species']= le.fit_transform(df['Species'])
df['Species'].unique()

X=df.iloc[:,:4]
y=df.iloc[:,4:]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=123)

svm = SVC(kernel="rbf", gamma=0.5, C=1.0)
svm.fit(X_train, y_train)
y_prediction=svm.predict(X_test)

class_names=["Iris-setosa","Iris-virginica","Iris-versicolor"]
print(classification_report(y_test, y_prediction ,target_names=class_names))


x=df.iloc[:,:2]
svm2 = SVC(kernel="rbf", gamma=0.5, C=1.0)
svm2.fit(x,y)
DecisionBoundaryDisplay.from_estimator(
		svm2,
		x,
		response_method="predict",
		cmap=plt.cm.Spectral,
		alpha=0.8,
	)
   
   """
   print(code)
