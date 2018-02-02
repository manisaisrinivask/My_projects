
# coding: utf-8

# In[24]:


'''creating list for common and non-common students'''
cmn_stu=[]
not_cmn=[]
'''py-python students ; web-web applications students'''
def common_stu(py,web):
    for stu in py:
        '''checking for common students'''
        if stu in web:
            cmn_stu.append(stu)
        else:
            not_cmn.append(stu)
    '''checking for remaning students in web applications class'''
    for stu in web:
        if stu not in cmn_stu:
            not_cmn.append(stu)
    print "students common in both classes are: " + str(cmn_stu)
    print "students not common in both classes are: " +str(not_cmn)

'''input'''
common_stu(['rahul','sachin','dhoni','gavaskar'],['rahul','saurav','shewag','kapil','dhoni'])
            

