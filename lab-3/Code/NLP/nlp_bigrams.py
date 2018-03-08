
# coding: utf-8

# In[27]:


#importing libraries
import re, collections
from nltk.tokenize import word_tokenize, wordpunct_tokenize, sent_tokenize
from nltk.stem import SnowballStemmer, WordNetLemmatizer
from nltk.tag import pos_tag
import sys
import nltk

# Reading the Text file
with open('sample_file.txt', 'r') as f:
    File_read = f.read()
    
def tokens(text):
    # Get all words from the corpus
    return re.findall('[a-z]+', text.lower())

Words = tokens(File_read)

# Implementation of the Lemmatization
lemmatizer = WordNetLemmatizer()
LemmatizedWords = [lemmatizer.lemmatize(word) for word in Words]
print (LemmatizedWords)

print ("\n------------------------------------------------")

#printing bi-grams
bigrm = list(nltk.bigrams(Words))
print("the bigrams are: ")
print (bigrm)

# Calculating the word frequency
WordCount = collections.Counter(bigrm)

Top5Words = WordCount.most_common(5)

TopWords = [word for (word, freq) in Top5Words]

print ('\n Top 5 bigrams with high frequency of occurrence: \n', str(TopWords))
# Implementing the word and sentence tokenization to extract the words in a sentence

Sentence = sent_tokenize(File_read)

print ('\nThe Sentences in the File are: \n', Sentence)



# Sentences with the Top5Words
lst=[]
for s in Sentence:
    Words=tokens(s)
    bigrm = list(nltk.bigrams(Words))
    for b in bigrm:
        if str(b) in str(TopWords):
            lst.append(s)
            break
print ("===============================================")
print ("These are the sentences with top bigrams: ")
print (lst)
print("=====================")
# Summary of the text
print ("The summary is:")
print(" ".join(lst))

