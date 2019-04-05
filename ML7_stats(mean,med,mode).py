
# coding: utf-8

# In[2]:


import random as rd
import numpy as np
x=np.random.randint(1,7,size=(500000,6))
print(x)


# In[3]:


x=np.random.randint(1,7,300000)#array(2d)
y=x.reshape(50000,6)#row vector
print(y)


# In[9]:


samplemean=np.mean(y,axis=1)
print(samplemean)


# In[10]:


print(samplemean.shape)


# In[12]:


samplemedian=np.median(y,axis=1)
print(samplemedian)


# In[13]:


print(samplemedian.shape)


# In[18]:


import scipy.stats as s
samplemode=s.mode(y,axis=1)#mode is not under numpy,it is imported through scipy
print(samplemode) #show mode and count its freq individually


# In[29]:


print(samplemode.mode) #only show mode
print(len(samplemode.mode))#mode function is not under numpy ,so shape is not used to check its dimension
#we can use len to check its dimension


# In[22]:


freqmean=s.itemfreq(samplemean)#unique values of mean(mostly repeated values)
print(freqmean)#first col represents unique values and 2 col represent freq


# In[31]:


freqmedian=s.itemfreq(samplemedian)
print(freqmedian)



# In[32]:


freqmode=s.itemfreq(samplemode)
print(freqmode)


# In[37]:


import matplotlib.pyplot as plt
plt.bar(freqmean[:,0],freqmean[:,1])#plot b/w all rows and 0 index col VS all rows and 1 col
plt.show()


# In[39]:


plt.bar(freqmedian[:,0],freqmedian[:,1])#plot b/w all rows and 0 index col VS all rows and 1 col
plt.show()
#more expanded on x axis , more variance


# In[40]:


plt.bar(freqmode[:,0],freqmode[:,1])#plot b/w all rows and 0 index col VS all rows and 1 col
plt.show()

