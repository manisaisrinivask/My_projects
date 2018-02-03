
# coding: utf-8

# In[37]:


import collections
inp=raw_input("enter a sentence: ")
lst=inp.split()
d=collections.defaultdict(int)
for ele in lst:
    d[ele]+=1
for ele in sorted(d):
    print ele,d[ele]
    


# In[41]:


def count_vow(inp):
    s=set('aeiouAEIOU')
    count=0
    for apl in inp:
        if apl in s:
            count +=1
    print "the number of vowels are: " +str(count)

count_vow("pyhton Program")
    


# In[39]:


from bs4 import BeautifulSoup
import urllib2

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
page = urllib2.urlopen(wiki)
soup = BeautifulSoup(page)
print soup.title
print soup.a
all_links=soup.find_all("a")
for link in all_links:
    print link.get("href")
all_tables=soup.find_all('table')
right_table=soup.find('table', attrs={'class' : "wikitable sortable plainrowheaders"})
right_table
tr = right_table.findAll('tr')
print "-----------------------------------------------"
for row in tr:
    cols = row.find_all('td')
    cols=[y.text.strip() for y in cols]
    print cols


