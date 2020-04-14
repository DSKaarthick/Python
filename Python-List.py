
# #  List

# In[22]:


lst1 = [90,20,30,70,80]
print(lst1)
print(type(lst1))


# In[23]:


lst2=[20,'Kaarthik',True,60]
print(lst2)
print(type(lst2))


# # Access List elements by slicing

# In[24]:


#Accessing the List Elements
print(lst1[0])
print(lst1[0:3])
print(lst1[:2])
print(lst1[0:])


# In[25]:


lst1.append(100)
print(lst1)
print(len(lst1))


# In[26]:


lst1.extend([120,150])
print(lst1)
print(len(lst1))


# In[49]:


lst1.pop(1) # remove elements based on index 
print(lst1)
lst1.remove(150)
print(lst1)


# In[28]:


print(lst1)


# In[55]:


lst2=[100,'Kaarthik',200]
print(lst2)
lst2.insert(300,3)
print(lst2)


# In[31]:


lst3=[lst1,40,lst2]
print(lst3)


# In[37]:


#Sorting the list elements
lst1.sort()
print(lst1)


# In[38]:


#Reverse the List Elements
lst1.reverse()
print(lst1)


# In[45]:


lst2=[100,'Kaarthik',200,300,400]
print(lst2)
#Deleting one element
del lst2[1]
print(lst2)
#deleting multiple elements
del lst2[1:2]


# In[46]:


print(lst2)


# In[47]:


#deleting entire list elements
del lst2


# # List Comprehension

# In[52]:


pow2=[]
for i in range(10):
    pow2.append(i**2)
 


# In[53]:


print(pow2)


# In[56]:


lst2=[3,4,5]
MulpliedLst2=[i*3 for i in lst2]
print(MulpliedLst2)


# In[58]:


low=['This','Is','Karthik']
newlow=[i[0] for i in low]
print(newlow)


# In[ ]:




