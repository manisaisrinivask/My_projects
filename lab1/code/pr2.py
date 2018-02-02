
# coding: utf-8

# In[11]:


usr_inp=raw_input("enter a sentence: ")
usr_inp=usr_inp.split()

"""calculating the half of length"""
half_len=len(usr_inp)/2
"""the words from mddle are taken"""
for word in range(half_len-1,half_len+1):
    print "the middle words are: " +usr_inp[word]

"""max with key as length"""
max_word=max(usr_inp,key=len)
print "this is the maximum length word: " +max_word

"""reversing every word in a sentence"""
rev_inp=[]
for word in usr_inp:
    """using slice to reverse and appending to a new lisr"""
    new_word=word[::-1]
    rev_inp.append(new_word)
"""joining back the list to get a new string"""
print " ".join(rev_inp)

