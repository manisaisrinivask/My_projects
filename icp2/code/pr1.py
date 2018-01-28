
# coding: utf-8

# In[47]:


def tuple_sort():
    inp1=["PHP","Exercises","Backend"]
    '''counting the length of each input'''
    len_inp1=[len(inp1[0]),len(inp1[1]),len(inp1[2])]
    '''converting into tuple'''
    new_inp1=list(zip(len_inp1,inp1))
    '''sorting using first key'''
    new_inp1.sort(key=lambda new_inp1:new_inp1[0])
    return new_inp1[2]
print(tuple_sort())

