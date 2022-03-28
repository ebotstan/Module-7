#!/usr/bin/env python
# coding: utf-8

# ### Exercise 1
# Ask a user to enter a number. If the number is positive, print <b>Positive number</b>. Otherwise, do not print any message. Finally, print 'goodbye' message at the end.

# In[2]:


number = int(input("Please enter a number: "))
if number > 0:
    print(f"This number {number}, is positive.")
print('Goodbye.')


# In[ ]:





# ### Exercise 2
# Ask for a code and store that answer. 
# If the answer is grey then print out if you found secret code.
# Otherwise print out the code is not the secret code.

# In[4]:


code = input("What is your code?: ")
if code == "grey" :
    print("You found the secret code.")
elif code != "grey" :        
    print(f"{code} is not the secret code.")


# In[ ]:





# ### Exercise 3
# 
# Ask a user to enter a phrase. If the word contains a number, display the "Number found" message. Otherwise, show the "Number not found" message. 

# In[30]:


phrase = input("Enter a phrase: ")

if ('0' in phrase) or ('1' in phrase) or ('2' in phrase) or ('3' in phrase) or ('4' in phrase) or ('5' in phrase) or ('6' in phrase) or ('7' in phrase) or ('8' in phrase) or ('9' in phrase) :
    print(f'Number found in "{phrase}.')
else :
    print(f'Number not found in {phrase}.')


# In[ ]:





# ### Exercise 4
# 
# Ask a user to enter a number. Then, only if the number is divisible by 2 and 3, show the result of the number divided by two and three in a formated string. The output should look something like this:
#         
#     Enter a number: 2
#     Bye    
#     
#     Enter a number: 60
#     60 / 2 = 30.0
#     60 / 3 = 20.0
#     Bye
#     
#     Enter a number: 3
#     Bye
#     
#     Enter a number: 10
#     Bye    

# In[42]:


number = int(input("Enter a number: "))
if number % 2 == 0 and number % 3 == 0 :
    print(f"{number} / 2 = {number/2}")
    print(f"{number} / 3 = {number/3}")
    
print("Bye")    


# In[ ]:





# ### Exercise 5
# Ask a user to enter a number. Determine if the number is zero, positive or negative. Use only <b>if</b> and <b>else</b> statements. 
#     

# In[49]:


number = int(input("Enter a number: "))
if number > 0 :
    print(f"The number {number}, is a positive number")
else :
    if number < 0 :
        print(f"The number {number}, is a negative number")
    else :    
        print(f"The number {number} (zero), is neither positive or negative.")
        


# In[ ]:




