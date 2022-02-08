#!/usr/bin/env python
# coding: utf-8

# # Machine learning with python
# ### Data type

# In[1]:


# Addition

10 + 2


# In[2]:


# Subtraction

10 - 2


# In[3]:


#Multiplication

10 * 2


# In[4]:


# Power

10 ** 2


# In[5]:


#Division - print reminder

10 / 2


# In[6]:


# Floor division - print reminder

10 // 2


# In[7]:


# Division

int((10) / 2)


# In[8]:


# Modulo division - print quotient

10 % 2


# In[9]:


# To print a string 3 times

3 * "_SK_"


# ### Check the data type

# In[10]:


# integers

type(1)


# In[11]:


# strings

type("Hello")


# In[12]:


# floating

type(1.0)


# In[13]:


# boolean

type(True)


# ### Variable Assignment

# In[14]:


a = 10
type(a)


# In[15]:


a = 10
b = 2
print((a*b)+(a/b)) #BODMAS rule


# ### various ways of printing

# In[16]:


print("Hello")


# In[17]:


f_name = "Kranthi"
l_name = "Potnuru"
print("My first name is {} and last name is {}".format(f_name,l_name))
print("My first name is {} and last name is {}".format(l_name,f_name))


# In[18]:


print("My first name is {first} and last name is {last}".format(first = f_name, last = l_name))


# ### Boolean variables
# . The output is either True or False

# In[19]:


type(True)


# In[20]:


type(False)


# In[21]:


#creating a string
my_str = "Kranthi Potnuru"


# In[22]:


# check all char are integers
print(my_str.isalnum())


# In[23]:


# check all char are alphabets
print(my_str.isalpha())


# In[24]:


# check if string contains are digits
print(my_str.isdigit())


# In[25]:


# check if string contains title
print(my_str.istitle())


# In[26]:


# check if string contains uppercase
print(my_str.isupper())


# In[27]:


# check if string contains lowercase
print(my_str.islower())


# In[28]:


# check if string contains spaces
print(my_str.isspace())


# In[29]:


# check if string starts with K
print(my_str.startswith("K"))


# In[30]:


# check if string ends with u
print(my_str.endswith("u"))


# ### Boolean and Logical Operators
# . and = True and True = True
# 
# . and = True and False = False  
#       
# . or  = True or True = True
# 
# . or  = True or False = True   

# In[31]:


a = "2612"
b = "kranthi"
a.isalnum() and b.isalpha()


# In[32]:


a = "Potnuru"
b = "kranthi"
a.isalnum() and b.isalpha()


# In[33]:


a = "2612"
b = "kranthi2612"
a.isalnum() and b.isalpha()


# In[34]:


a = "2612"
b = "kranthi"
a.isalnum() or b.isalpha()


# In[35]:


a = "2612"
b = "kranthi2612"
a.isalnum() and b.isalpha()


# ### Lists
# -> Data structure in python
# 
# -> represented by []
# 
# -> Mutable / changable
# 
# -> Ordered sequence

# In[36]:


type([])


# In[37]:


lst1 = []
type(lst1)


# In[38]:


lst2 = ['kranthi', 'sk', 26, 11]
type(lst2)


# In[39]:


len(lst2)


# ### Append
# -> Used to add elements inside a list, Adds element at the end of the list

# In[40]:


lst2.append("3")
print(lst2)


# In[41]:


# here it will give o/p as nested list
lst2.append(["June","Dec"])
print(lst2)


# In[42]:


# indexing
lst2[1]


# In[43]:


lst2[:]


# In[44]:


lst2[1:3]


# In[45]:


lst2[:2]


# In[46]:


lst2[2:3]


# ### Insert

# In[47]:


# insert at specific position
lst2.insert(5,"Nov")
print(lst2)


# ### Extend
# ->in append() if we add element it will give o/p as nested list but here it is not like that

# In[48]:


lst2.extend([4,17])
print(lst2)


# In[49]:


### Various operations that we can perform on list
lst = [1,2,3,4,5]


# In[50]:


sum(lst)


# In[51]:


lst.pop()


# In[52]:


lst


# In[53]:


lst.pop(0)


# In[54]:


lst


# In[55]:


lst3 = [1,1,1,2,2,3,4,5]


# In[56]:


lst3.count(1)


# In[57]:


len(lst3)


# In[58]:


lst3.index(1,0,4)


# In[59]:


min(lst3)


# In[60]:


max(lst3)


# In[61]:


lst3 * 2


# ### Sets
# -> Unordered collection of data
# 
# -> iterable, Mutable
# 
# -> No duplication of data
# 
# -> This is based on data structure known as hash table
# 
# -> Doesnot support indexing

# In[62]:


set_var = set()
print(set_var)


# In[63]:


type(set_var)


# In[64]:


set1 = {1,2,3,4,3}
print(set1)


# In[65]:


set1.add("k")
print(set1)


# In[66]:


set2 = {1,2,3,4,3}
print(set2)


# In[67]:


#set1 = {1,2,3,4,"k"}
#set2 = {1,2,3,4}
# Difference
#set2.difference(set1)


# In[68]:


set1 = {1,2,3,4,"k"}
set2 = {1,2,3,4}
set2.intersection(set1)


# In[69]:


set2.intersection_update(set1)


# ### Dictionary
# -> Unordered
# 
# -> Changable
# 
# -> Indexed
# 
# -> have keys and values

# In[70]:


dic = {}
type(dic)


# In[71]:


my_dict = {"abc": "cse", "bcd": "B", "cdf" : "kranthi"}
print(my_dict)


# In[72]:


type(my_dict)


# In[73]:


my_dict["abc"]


# In[74]:


for x in my_dict:
    print(x)


# In[75]:


for x in my_dict.values():
    print(x)


# In[76]:


for x in my_dict.items():
    print(x)


# In[77]:


my_dict["l_name"]="Potnuru"
print(my_dict)


# ### Tuple
# -> unchangable

# In[78]:


my_tuple = ("K","s","sk")


# In[79]:


my_tuple[0]


# In[80]:


type(my_tuple)


# In[81]:


my_tuple.count("k")


# In[82]:


my_tuple.index("sk")

