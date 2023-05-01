#!/usr/bin/env python
# coding: utf-8

# In[1]:


#if,elif and else


# In[2]:


#if some_condition:
 #do_something
    #else:
    #do_something else


# In[3]:


if True:
    print("It's True")


# In[4]:


if 3<2:
    print("It's True")


# In[12]:


hungry = False
if hungry:
    print('FEED ME!') 
elif hungry:
    print('iamhungry')
elif hungry:
    print("FEED MEEE")
    
else:
    print("I'm not hungry")


# In[14]:


loc = 'abcd'
if loc == 'Auto shop':
    print ('cars are cool')
elif loc == 'Bank':
    print ('money is cool')
elif loc == 'Store':
    print ('welcome to the store')
else:
    print ('I do not know much!')


# 

# In[16]:


name = 'asdasd'
if name == 'Lakpa':
    print (' practice prog everyday')
elif name == 'Pavas':
    print ('Concentrate more')
elif name == 'Superman':
    print ('He can fly')
else:
    print ('We have nothing to say')


# In[17]:


#For loops


# In[19]:


#syntax of a for loop
my_iterable = [1,2,3]
for item in my_iterable:
    print (item) 


# In[20]:


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    print ('I am good')


# In[21]:


mylist = [1,2,3,4,5,6,7,8,9,10]
for num in mylist:
    if num%2 == 0:
        print (num)
    else:
        print(f'odd number : {num}')


# In[1]:


mylist = [1,2,3,4,5,6,7,8,9,10]
list_sum = 0
for num in mylist:
    list_sum = list_sum + num
    print(list_sum)


# In[2]:


mystring = 'Hello World'
for letter in mystring:
    print(letter)


# In[4]:


for _ in 'Medhavi':
    print ('Happy')
    


# In[6]:


tup = (1,2,3)
for item in tup:
    print(item)


# In[7]:


mylist = [(1,2),(3,4),(5,6),(7,9),(10,11)]
for (a,b) in mylist:
    print(a)
    print(b)


# In[8]:


mylist = [(1,2),(3,4),(5,6),(7,9),(10,11)]
for b,a in mylist:
    print(a)
     #print(b)


# In[9]:


mylist = [(1,2,4),(6,7,8),(11,12,13)]
for fv1,fv2,fv3 in mylist:
    print (fv2)
    print (fv3)
    print (fv1)


# In[14]:


d = {'k1':1,'k2':2,'k3':3}
for item in d. keys():
    print (item)


# In[16]:


d = {'k1':1,'k2':2,'k3':3}
for item in d.values():
    print(item)


# In[17]:


d = {'k1':1,'k2':2,'k3':3}
for key,value in d:
    print (value)


# In[19]:


d = {'k1':1,'k2':2,'k3':3}
for value in d.values ():
    print (value)


# In[ ]:


#while loops in Python

