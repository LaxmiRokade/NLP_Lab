##Assignment No.02##
#Name:Rokade Laxmi Malhari
##Roll No:49
#Batch:B3
#Title:Assignment to implement Bag of Words and TFIDF using Gensim library.
import gensim
from gensim import corpora
from gensim.utils import simple_preprocess


text1 = ["""The Dog sat
         The Dog sat in the hat
         The Dog sat with the hat."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)


print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)

g_bow =[g_dict1.doc2bow(token, allow_update = True) for token in tokens1]
print("Bag of Words : ", g_bow)

text = ["""The Dog sat
         The Dog sat in the hat
         The Dog sat with the hat."""]

g_dict = corpora.Dictionary([simple_preprocess(line) for line in text])
g_bow = [g_dict.doc2bow(simple_preprocess(line)) for line in text]

print("Dictionary : ")
for item in g_bow:
    print([[g_dict[id], freq] for id, freq in item])
    
##OUTPUT##
'''
Output for Bag of Words:
{'Dog': 0, 'The': 1, 'hat': 2, 'hat.': 3, 'in': 4, 'sat': 5, 'the': 6, 'with': 7}
Bag of Words :  [[(0, 3), (1, 3), (2, 1), (3, 1), (4, 1), (5, 3), (6, 2), (7, 1)]]

Output for TFIDF:
Dictionary : 
[['dog', 3], ['hat', 2], ['in', 1], ['sat', 3], ['the', 5], ['with', 1]]
'''