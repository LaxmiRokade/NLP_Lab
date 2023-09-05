##Assignment No.01##
#Name:Rokade Laxmi Malhari
##Roll No:49
#Batch:B3
#Title:"Text Pre-Processing using NLP operations:perform Tokenization
# Stop word removal,Lemmatization ,Part-of-Speech Tagging use any sample text"

#import Libraries
import spacy
#language model loaded
nlp = spacy.load("en_core_web_sm")
about_text = (
   "Natural language processing (NLP) is a field  of computer science, artificial intelligence"
    "concerned with the interactions between computers and human"
)
##1-------Tokenization---------##

about_doc = nlp(about_text)

for token in about_doc:
    print (token, token.idx)


##2-------Stop Words-----------###

about_doc = nlp(about_text)
print([token for token in about_doc if not token.is_stop])


##3-------Lemmatization-----------##

about_doc=nlp(about_text)
for token in about_doc:
    if str(token) != str(token.lemma_):
        print(f"{str(token):>20} : {str(token.lemma_)}")
        

 ##4-------Part of Speech----------##   
               
about_doc = nlp(about_text)
for token in about_doc:
    print(
        f"""
TOKEN: {str(token)}
=====
TAG: {str(token.tag_):10} POS: {token.pos_}
EXPLANATION: {spacy.explain(token.tag_)}"""
    )
 
 ##------------------OUTPUT---------------##
"""
1.Tokenization
Output:
Natural 0
language 8
processing 17
( 28
NLP 29
) 32
is 34
a 37
field 39
of 45
computer 48
science 57
, 64
artificial 66
intelligence 77
concerned 88
with 97
the 102
interactions 106
between 118
computers 127
and 137
human 141

2.Stop Words:
Output:
[Natural, language, processing, (, NLP, ), field, computer, science, ,, artificial, intelligence, concerned, interactions, computers, human]
3. Lemmatization:
Output:
        processing : processing
               ( : (
             NLP : NLP
               ) : )
                is : be
                a : a
             field : field
               of : of
         computers : computer
             human : human
4. Part of Speech:
Output:
TOKEN: Natural
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective

TOKEN: language
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

TOKEN: processing
=====
TAG: NN         POS: NOUN
EXPLANATION: noun, singular or mass

...

TOKEN: computers
=====
TAG: NNS        POS: NOUN
EXPLANATION: noun, plural

TOKEN: and
=====
TAG: CC         POS: CCONJ
EXPLANATION: coordinating conjunction

TOKEN: human
=====
TAG: JJ         POS: ADJ
EXPLANATION: adjective
"""