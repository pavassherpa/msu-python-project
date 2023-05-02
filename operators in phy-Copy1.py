#!/usr/bin/env python
# coding: utf-8

# In[1]:


mylist = [1,2,3,4,5,6,7,8,9,10]


# In[2]:


for num in range (0,10):
    print (num)


# In[3]:


list(range(0,10))


# In[4]:


for num in range (10):
    print(num)
    


# In[5]:


for num in range (3,10):
    print (num)


# In[6]:


for num in range (0,11,2):
    print(num)


# In[7]:


#enumerate


# In[9]:


index_count = 0
for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count,letter))
    index_count +=1


# In[11]:


word = 'abcde'
for index,letter in enumerate (word):
    print (index)
    print (letter)
    print ('\n')


# In[16]:


#zip function


# In[19]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3]
for item in zip (mylist1,mylist2):
    print(item)


# In[26]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3]
for l1,l2 in zip(mylist1,mylist2):
    print(l1)
    print(l2)


# In[28]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3,4,5]
list (zip (mylist1,mylist2))


# In[29]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3,4,5]
mylist3 = [11,22,33]
for item in zip (mylist1,mylist2,mylist3):
    print (item)


# In[31]:


mylist1 = ['a','b','c']
mylist2 = [1,2,3,4,5]
mylist3 = [11,22,33]
for l1,l2,l3 in zip (mylist1,mylist2,mylist3):
    print(l1)
    print(l2)
    print(l3)


# In[32]:


#in keyword


# In[33]:


'x' in [1,2,3]


# In[34]:


'x' in ['x','y','z']


# In[35]:


'a' in 'wonderla'


# In[36]:


'mykey' in {'mykey':1}


# In[37]:


d = {'mykey':345}


# In[38]:


345 in d.values()


# In[40]:


345 in d.keys() 


# In[42]:


345 in d.items()


# In[43]:


#min,max


# In[44]:


mylist = [10,20,30,40,50,60]
min(mylist)


# In[45]:


max(mylist)


# In[ ]:




