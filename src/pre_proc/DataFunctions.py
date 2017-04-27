'''
Created on Apr 25, 2017

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
import pickle
if __name__ == '__main__':
    
    in_df = PullFunctions.pull_from_url(DataConstants.data_url)
    for col in DataConstants.train_columns:
        X, y = in_df[col], in_df[DataConstants.pred_column]
       
        Xtrain, Xvalidate, ytrain, yValidate = train_test_split(X, y, train_size=0.7)
        try:
            vect = pickle.load(open('../../resources/vectorizers/'+col+'_vect.pickle','rb'))
        except Exception as e:
            
            vect = TfidfVectorizer(stop_words='english',sublinear_tf=True)
        
        tdm = vect.fit_transform(Xtrain, ytrain)
    
        try:
            clf = pickle.load(open('../../resources/classifiers/'+col+'_clf.pickle','rb'))
        except Exception as e:
            
            clf  = RandomForestClassifier()
        
        clf.fit(tdm,ytrain)
        
        pipeline = Pipeline([
        ('vect', vect),
        ('clf', clf)
        ])
        ''''vect__max_df': [0.25, 0.5, 0.6, 0.7, 1.0],
            'vect__ngram_range': [(1, 1), (1, 2), (2,3), (1,3), (1,4), (1,5)],
            'vect__use_idf': [True, False]
        '''
        parameters={
            
        }
        gridSearchClassifier=GridSearchCV(pipeline, parameters, n_jobs=3, verbose=1, scoring='accuracy')
        gridSearchClassifier.fit(Xtrain, ytrain)
        
        print ('best score: %0.3f' % gridSearchClassifier.best_score_)
        # Calculate best set of parameters for gridSearchClassifier
        bestParameters = gridSearchClassifier.best_estimator_.get_params()
        # Display best set of parameters
        print ('best parameters set:')
        print (bestParameters)
            
        # Make predictions on validation set and evaluate performance of gridSearchClassifier
        predictions = gridSearchClassifier.predict(Xvalidate)
        print ('Accuracy:', accuracy_score(yValidate, predictions))
        pickle.dump(vect,open('../../resources/vectorizers/'+col+'_vect.pickle','wb'))

        pickle.dump(clf,open('../../resources/classifiers/'+col+'_clf.pickle','wb'))
        