
# coding: utf-8

# In[5]:


import re
inp= raw_input("Input your password: ")
a = True
while a:  
    if (len(inp)<6 or len(inp)>16):
        break
    elif not re.search("[a-z]",inp):
        break
    elif not re.search("[0-9]",inp):
        break
    elif not re.search("[A-Z]",inp):
        break
    elif not re.search("[[$@!*]",inp):
        break
    else:
        print "Valid Password"
        a=False
        break

if a:
    print "Not a Valid Password"

