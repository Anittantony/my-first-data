#!/usr/bin/env python
# coding: utf-8

# <h1 style="color:Brown"> Tuples </h1>
# 
# - Tuples are an ordered sequnce of mixed data types.
# - Tuples are written as comma-separated  elements within parenthesis
# 

# In[1]:


t= ("disco", 12, 4.5)

t


# In[2]:


type(t)


# <h3> Tuples can be defined is various ways </h3>

# #### A tuple can be defined without using parenthesis 

# In[1]:


sample_tuple= 1,2,3,4

print(sample_tuple)
type(sample_tuple)


# ### Indexing in tuples

# In[1]:


t = ("Mumbai", 84, "Python")


# gives the element at index location 1.
print(t[1])


# gives the last element from tuple.
print(t[-1])


# In[2]:


t[2][1]


# In[3]:


t[-1][-5]


# ### Slicing

# In[1]:


# Slicing first 3 elements from t.

t= ("Mumbai", 84, "Python", 5, 2, 1)

t[0:3]


# In[1]:


# or,
t[ :3]


# In[8]:


# Slicing last 2 elements from t.

t[-2:]
# or,
t[ :3]


# In[9]:


# no.of elements in tuple t.

len(t)


# #### Concatenating tuples

# In[10]:


tup1= ("This", "is", "Session")
tup2= ("on", "Tuples")


# adding contents of 'tup2 to tup1' and storing in tup3
tup3= tup1 + tup2
tup3


# #### sum() - min() - max()

# In[2]:


t= (2, 4, 3, 5, 7)


print(sum(t))
print(min(t))
print(max(t))


# In[2]:


t_1= (2, 4, 3, 5, 7)
t_2= (1, 6, 9, 3, 2)


t_1 + t_2


# ### Immutability of Tuples

# In[13]:


t = ("USA", 4, 3, "Disco", 7.5)

t[3] = "Rock"


# In[14]:


# Nested Tuples

t= (1, 5, "Disco", ("Python", "Java"))

# Access "Java" from the nested tuple
t[3][1]


# <h1 style="color:Brown"> Lists </h1>
# 
# - Lists are an ordered sequnce of mixed data types.
# - Lists are written as comma-separated  elements within square brackets

# In[15]:


L= ["India", 23, 6, "Mumbai"]

print(L)
type(L)


# In[16]:


# Nested List (List within a List is called 'Nested_List'.)

L= ["Chemistry", "Biology", [1989, 2004], ["Oreily", "Pearson"]]
L


# In[17]:


# Indexing

print(L[1])
print(L[-3])
print(L[0:3])         #--->(upper limit not included)


# In[18]:


# Replace "Biology" with "Physics"

L[1]= "Physics"
L


# In[19]:


# List Concatanetion

L= L + [5, 8]

L


# In[20]:


# extend()

L= ["Chemistry", "Biology", 1989, 2004, "Oreily", "Pearson"]

L.extend([5, 8])
L


# In[21]:


# append()

L= ["Chemistry", "Biology", 1989, 2004, "Oreily", "Pearson"]

L.append([5, 8])
L


# In[22]:


# pop() 

L= ["Chemistry", "Biology", 1989, 2004, "Oreily", "Pearson"]

L.pop()
L


# In[23]:


# same as above cell.

L= ["Chemistry", "Biology", 1989, 2004, "Oreily", "Pearson"]

L.pop(-2)
L


# In[24]:


# remove()

L= ["Chemistry", "Biology", 1989, 2004, "Oreily", "Pearson"]
L.remove("Oreily")
L


# In[25]:


# remove()

L.remove()

L


# In[26]:


# Sorting Lists

mylist= [32, 24, 65, 9, 15]

sorted(mylist)


# In[27]:


mylist


# In[28]:


new_list= sorted(mylist)

new_list


# In[ ]:





# In[2]:


mylist= [32, 24, 65, 9, 15]

mylist.sort()


# In[3]:


mylist


# In[ ]:





# In[ ]:


mylist= [32, 24, 65, 9, 15]

mylist.sort(reverse=True)

mylist


# In[ ]:


help( sorted )


# In[ ]:


help(list.sort)


# In[ ]:





# ## Dictionaries

# In[4]:


# Creating a dictionary

d= {"India": "INR", "USA": "USD", "France": "Euros"}

# Access value using keys
d


# In[5]:


# to get the keys.

d.keys()


# In[6]:


# to get the values.

d.values()


# In[35]:


# Replace the value for a key into a dictionary.

d["India"]= "Rs"
d


# In[36]:


# adding to the Dictionary. 

d["Japan"]= "Yen"
d


# In[37]:


# sorting "Keys" of above dictionary.

sorted(d)


# ### Dictionary

# In[7]:


# create a dictionary

data_science = {'Tool' : ['Python', 'R', 'SQL'], 
                'Expert' : ['Martha', 'James', 'Albert'],
                'Institute' : ['Imarticus', 'Upgrad', 'Amity'],
                'Location' : ['Delhi', 'Banglore', 'Mumbai']
                }

data_science


# In[8]:


# creating a DataFrame from a dictionary.

import pandas as pd

df= pd.DataFrame(data_science)
df


# In[ ]:





# In[ ]:




