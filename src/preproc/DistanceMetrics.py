'''
Created on May 11, 2017

@author: abhijit.tomar
'''
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def fill_cosine_sims(input_df,v_of_i,secondary_col,vect):
    
    vect_mat_of_col = vect.transform(input_df[secondary_col])
    
    return [cosine_similarity(v_of_i[i], vect_mat_of_col[i])[0][0] for i in range(v_of_i.shape[0])]

def populate_distance_metrics(in_df, col_list, id_col):
    col_list.remove(id_col)
    vect_data=in_df[col_list[0]].map(str)
    
    for idx,col in enumerate(col_list):
        if idx==0:
            continue;
        vect_data = vect_data + " " + in_df[col].map(str)
       
    cv = CountVectorizer(stop_words='english', max_features=1000)
    # Learn a vocabulary dictionary of all tokens in search term, product title, description and bullets
    cv.fit(vect_data)
    print ('cv fit')
    # Initialize TfidfVectorizer
    tiv = TfidfVectorizer(ngram_range=(1, 3), stop_words='english', max_features=1000)
    # Learn vocabulary and idf of the words in search term, product title, description and bullets
    tiv.fit(vect_data)
    print ('tiv fit')
    key_set=set()
    cols_to_keep=[]
    # For each column
    for i in range(len(col_list)):
        for j in range(len(col_list)):
            if i==j:
                continue;
            col_key=col_list[i]+col_list[j]
            rev_col_key=col_list[j]+col_list[i];
            if col_key not in key_set and rev_col_key not in key_set:
                key_set.add(col_key)
                key_set.add(rev_col_key)
                # Transform search terms to document-term matrix with counts as values
                cv_of_i = cv.transform(in_df[col_list[i]])
                # Transform search terms to document-term matrix with tf idf scores as values
                tiv_of_i = tiv.transform(in_df[col_list[i]])
                # Add cosine similarity between count vectors of search term and the column as a new feature
                in_df['cv_cos_sim_'+col_list[i]+'_'+col_list[j]]=fill_cosine_sims(in_df, cv_of_i, col_list[j], cv)
                print ('cv transformed ',col_list[i],col_list[j])
                cols_to_keep.append('cv_cos_sim_'+col_list[i]+'_'+col_list[j])
                # Add cosine similarity between tfidf vectors of search term and the column as a new feature
                in_df['tiv_cos_sim_'+col_list[i]+'_'+col_list[j]]=fill_cosine_sims(in_df, tiv_of_i, col_list[j], tiv)
                print ('tiv transformed ',col_list[i],col_list[j])
                cols_to_keep.append('tiv_cos_sim_'+col_list[i]+'_'+col_list[j])
        
    cols_to_keep.append(id_col)
    print (in_df.columns.values)
    print(in_df.head(2))
    return in_df,cols_to_keep