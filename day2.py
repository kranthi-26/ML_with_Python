#!/usr/bin/env python
# coding: utf-8

# ### Numpy

# In[1]:


import numpy as np


# In[2]:


lst = [1,2,3,4,5]
arr = np.array(lst)


# In[3]:


type(arr)


# In[4]:


print(arr)


# In[5]:


arr   # 1D array -> ( [] )


# In[6]:


arr.shape


# In[7]:


# to convert Multi dimensional array
lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,6]
lst3 = [1,2,3,4,7]
arr = np.array([lst1,lst2,lst3])


# In[8]:


arr


# In[9]:


arr.shape


# In[10]:


arr.reshape(5,3)


# ### Indexing

# In[11]:


# Accessing the array element
arr = np.array([1,2,3,4,5,6,7,8,9])


# In[12]:


arr[3]


# In[13]:


arr


# In[14]:


arr.reshape(3,3)


# In[15]:


lst1 = [1,2,3,4,5]
lst2 = [1,2,3,4,6]
arr = np.array([lst1,lst2])


# In[16]:


arr


# In[17]:


arr[1,2]  # [row index, column index]


# In[18]:


arr[0:2,0:2]


# In[19]:


arr[0:3,3:]


# In[20]:


arr[0:2,2:4]


# In[21]:


arr = np.arange(0,10)


# In[22]:


arr


# In[23]:


arr = np.arange(0,10,step=2)


# In[24]:


arr


# In[25]:


np.linspace(1,10,50)


# ### Copy function

# In[26]:


arr[3:]=100


# In[27]:


arr


# In[28]:


arr1 = arr


# In[29]:


arr1[3:]=100


# In[30]:


arr1


# In[31]:


arr1[3:]=500


# In[32]:


arr1


# In[33]:


arr


# In[34]:


arr1=arr.copy()


# In[35]:


print(arr)
arr1[3:]=1000
print(arr1)


# In[36]:


arr


# In[37]:


val = 2


# In[38]:


arr<2


# In[39]:


arr*2


# In[40]:


arr/2


# In[41]:


np.ones(4)


# In[42]:


np.ones(4,dtype=int)


# In[43]:


np.random.rand(3,3)


# In[44]:


np.random.randn(3,3) #standard random distributuin


# In[45]:


np.random.randint(0,100,8) # select any 8 numbers between 0 to 100


# In[46]:


np.random.random_sample((1,5))


# ### Pandas

# In[47]:


import pandas as pd
import numpy as nd


# In[50]:


df = pd.DataFrame(np.arange(0,20).reshape(5,4), index = ["row1","row2","row3","row4","row5"], columns = ["column1","column2","column3","column4"])


# In[51]:


df.head()


# In[52]:


df.to_csv("test1.csv")    # to convert the above table into excel sheet


# In[54]:


# Accessing the elements
# Loc -> focus on row index
df.loc["row1"]


# In[55]:


type(df.loc["row1"])


# In[57]:


# [row index,column index]
df.iloc[1,2]


# In[58]:


df.iloc[0:2,0:2]


# In[59]:


type(df.iloc[0:2,0:2])


# In[60]:


df.iloc[0:2,0:1]


# In[61]:


df.iloc[0:2,2:]


# In[62]:


df.iloc[:,1:]


# In[63]:


df.iloc[:,1:].values # DataFrame into array


# In[64]:


df.iloc[:,1:].values.shape


# In[65]:


# checking null values
df.isnull().sum()


# In[66]:


df


# In[69]:


df["column1"].value_counts()


# In[70]:


df["column1"].unique()


# In[71]:


df["column3"]


# In[72]:


df[["column3", "column4"]]


# ### Pandas read operation

# In[73]:


df = pd.read_csv("mercedesbenz.csv")  # csv = comma seperated values


# In[74]:


df.head() # by using this we can see top 5 rows of data


# In[75]:


df.info() 


# In[76]:


df.describe() # skip categorical data


# In[79]:


df["y"].value_counts()


# # CSV

# In[81]:


from io import StringIO, BytesIO


# In[83]:


data = ("col1,col2,col3\n"
       "x,y,1\n"
       "a,b,2\n"
       "c,d,3")


# In[84]:


type(data)


# In[85]:


pd.read_csv(StringIO(data))


# In[87]:


df = pd.read_csv(StringIO(data), usecols=["col1","col2"])


# In[88]:


df


# In[89]:


df.to_csv("test.csv") # to covert above DF into .csv file


# In[91]:


df["col1"]


# In[92]:


df["col1"][1]

