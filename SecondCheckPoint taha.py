#!/usr/bin/env python
# coding: utf-8

# # Question 1 

# In[21]:

#what i tried doin
for x in range(2002, 3201, 7):
if x%5!=0 :
    print(x)


# In[17]:


print(2000%7)


# In[3]:


print(2002%7)


# In[22]:

#what i found out is true
nl=[]
for x in range(2002, 3201):
    if (x%7==0) and (x%5!=0):
        nl.append(str(x))
print (','.join(nl))


# # Question 2

# In[4]:


func = lambda a,b,c : a*b*c
print(func(2, 3, 4))


# # Question 3

# In[5]:


n=int(input("Enter a number:"))
d={x:x*x for x in range(1,n+1)}
print(d)


# # Question 4

# In[16]:


def Myfunc(str, n):
    firstpart = str[:n]
    secondpart = str[n+1:]
    return firstpart + secondpart
print(Myfunc("isra", 0))


# # Question 5

# In[7]:


import numpy as np
a = np.array([[0, 1],[2, 3]])
print(a)
print(a.tolist())


# # Question 6

# In[8]:


import numpy as np
x = np.array([0, 1, 2])
y = np.array([2, 1, 0])
print(np.cov(x, y))


# # Question 7

# In[18]:


import math

C= 50
H = 30
Ds = []
result =[]
Dv=input("enter the value of D\n")
Ds=Dv.split(",")
Ds = [int(i) for i in Ds]
i=0
l = len(Ds)
while(i<l):
    Q = round(math.sqrt((2*C*Ds[i])/H))
    result. append(Q)
    i+=1
print("output=",result)


# In[ ]:




