#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
df = pd.read_csv("C:\\Users\\Smit\\OneDrive\\Desktop\\DATASET\\GOI.csv")
df.head(10)


# In[2]:


df.isna().sum()


# In[3]:


import matplotlib.pyplot as plt
plt.hist(df['Literacy Rate (Persons) - Total - 2001'],bins=30,color='skyblue')
plt.hist(df['Literacy Rate (Persons) - Total - 2011'])
plt.hist(df['Literacy Rate (Persons) - Rural - 2001'])
plt.hist(df['Literacy Rate (Persons) - Rural - 2011'])
plt.hist(df['Literacy Rate (Persons) - Urban - 2001'])
plt.hist(df['Literacy Rate (Persons) - Urban - 2011'])
plt.xlabel('Literacy rate')
plt.show()


# In[4]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Total - 2001'], bins=30, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2001")
plt.xlabel("literacy rate")
plt.show()


# In[5]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Total - 2011'], bins=40, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2011")
plt.xlabel("literacy rate")
plt.show()


# In[6]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Rural - 2001'], bins=30, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2011")
plt.xlabel("literacy rate")
plt.show()


# In[7]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Rural - 2011'], bins=30, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2011")
plt.xlabel("literacy rate")
plt.show()


# In[8]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Urban - 2001'], bins=30, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2011")
plt.xlabel("literacy rate")
plt.show()


# In[9]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Urban - 2011'], bins=30, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2011")
plt.xlabel("literacy rate")
plt.show()


# In[10]:


plt.figure(figsize=(8, 5))
sns.histplot(df['Literacy Rate (Persons) - Total - 2011'], bins=30, kde=True, color='skyblue')
plt.title("Literacy Rate (Persons) - Total - 2011")
plt.xlabel("literacy rate")
plt.show()


# In[ ]:




