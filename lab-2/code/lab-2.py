
# coding: utf-8

# ### Problem-1

# Consider a shop UMKC with dictionary of all book items with their prices. Write a program to 
# find the books from the dictionary in the range given by user. a

# In[45]:


# giving names of books and prices in a dictionary called d
d={"python":20,"web":40,"c":30,"java":10}
lst=[]
# books in range of 10 and 20
for k,v in d.iteritems():
    if v>=10 and v<=20:
        lst.append(k)
print "these are the books you can buy: " + " ".join(str(x)for x in lst)


# ## Problem-2

# With any given number n,  
# In any mobile , there is contact list. Create a list of contacts and then prompt the user to do the 
# following: 
# a)Display contact by name 
# b)Display contact by number 
# c)Edit contact by name 
# d)Exit 

# In[85]:


# creating a contact list with list
inp=[{"name":'c',"number":3333333333,"email":"c@gmail.com"},{"name":"a","number":1111111111,"email":"a@gmail.com"},
     {"name":"b","number":2222222222,"email":"b@gmail.com"}, {"name":"d","number":4444444444,"email":"d@gmail.com"}]

# Sorting b_name
def by_name(inp):
    lst=[]
    # Searching foe name
    for ele in range(len(inp)):
            lst.append(inp[ele]["name"])
    # Sorting them
    return sorted(lst)

# Sorting by number
def by_number(inp):
    lst=[]
    # Searching for number
    for ele in range(len(inp)):
        lst.append(inp[ele]["number"])
    # Sorting them 
    lst.sort()
    return lst

# Edit contact by name
def edit_name(inp,given_name,modified_number):
    for ele in range(len(inp)):
        # checking for the given name
        if inp[ele]["name"]==given_name:
            #modifing number
            inp[ele]["number"]=modified_number
            print "modified list is: "+str(inp[ele])
            
# exiting and printing all the modified contact list
def exit():
    print "exited"
    for ele in range(len(inp)):
        print inp[ele]
        
        

#driver functions
print by_name(inp)
print by_number(inp)  
edit_name(inp,"a",6666666666)
exit()


# ## Problem-4

# Using Numpy create random vector of size 15 having only Integers in the range 0 -20. Write a 
# program to find the most frequent item/value in the vector list.

# In[95]:


import numpy as np
# creating random number with max number as 5 and size=15
a = np.random.randint(5,size=15)
print a
# counting the most frequent element
counts = np.bincount(a)
print "the most frequent number is :" +str(np.argmax(counts))

