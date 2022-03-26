#!/usr/bin/env python
# coding: utf-8

# In[3]:


#print positive numbers in a range
n=int(input("enter a number to be set as range"))
for i in range(0,n+1):
    print(i)


# In[5]:


#fibonnaci series
n=int(input("enter a number to be set as range"))
a=0
b=1
if n==0:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        print(c)


# In[ ]:




