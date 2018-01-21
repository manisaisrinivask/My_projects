
# coding: utf-8

# In[15]:


import random
"""using random module randomly take a number form 0 to 9"""
num=random.randint(0,9)
print("Rules: The computer guesses a number between 0 and 9. You should gusess that number correctly")
print("The computer displays if you guessed it correct or above or below the computer generated number ")
uinp=int(input("enter you guessed number: "))
"""conditional statements"""
if uinp>num:
    print("your answer is higher than required ")
if uinp<num:
    print("your answer is lower than required")
if uinp==num:
    print("Congrats!! You guessed it right")
    
      

