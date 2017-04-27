'''
Created on Apr 26, 2017

@author: abhijit.tomar
'''
from sklearn.cross_validation import train_test_split
from pull import PullFunctions
from constants import DataConstants
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.pipeline import Pipeline
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import VotingClassifier
import pickle
import numpy
if __name__ == '__main__':
    in_df = PullFunctions.pull_from_url(DataConstants.data_url)
    X, y = in_df[DataConstants.train_columns].as_matrix(), in_df[DataConstants.pred_column]
    
    vect = TfidfVectorizer(stop_words='english',sublinear_tf=True)
        
    tdm = vect.fit_transform(X, y)
    clf_tup_list = []
    clf_list=[]
    for col in DataConstants.train_columns:
        clf = pickle.load(open('../../resources/classifiers/'+col+'_clf.pickle','rb'))
        clf_tup_list.append((col+'_clf',clf))
        clf_list.append(clf)
        
    eclf = VotingClassifier(estimators=clf_tup_list, voting='hard')
    clf_list.append(eclf)
    for clf, label in zip(clf_list, DataConstants.train_columns):
        scores = cross_val_score(clf, tdm, y, cv=5, scoring='accuracy')
        print("Accuracy: %0.2f (+/- %0.2f) [%s]" % (scores.mean(), scores.std(), label))