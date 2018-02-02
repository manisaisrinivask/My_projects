
# coding: utf-8

# In[8]:


'''import itertools'''
from itertools import combinations
'''creating two lists'''
lst_permu=[]
ans_lst=[]

'''fuction which returns triplets, if any'''
def triplets(lst):
    '''creating a list of tuples in combinations of three'''
    lst_permu=list(combinations(lst,3))
    for ele in lst_permu:
        sum=0
        for num in ele:
            sum=sum+num
        '''checking if sum of each element in tuple is zero'''
        if sum==0:
            ans_lst.append(ele)
            
    return ans_lst

'''giving input'''
print triplets([1,3,6,2,-1,2,8,-2,9])   

