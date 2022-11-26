#!/usr/bin/env python
# coding: utf-8

# ###### Assessment

# ###### I am going to provide two .csv files , you are supposed to work on them and have to provide solutions to the following problems

# ###### import necessary libraries

# In[67]:


import pandas as pd


# ###### merge those two csv files (after getting as dataframes, get them as a single dataframe)

# In[68]:


df = pd.read_csv("D:\\DOWNLOADS\\college_1.csv")
df1 = pd.read_csv("D:\\DOWNLOADS\\college_2.csv")


# In[69]:


data = pd.concat([df, df1], ignore_index=True)
data


# ###### Take each csv file , split that csv file into multiple categories (example csv files are added in the repo) 
# 

# ###### consider if the codekata score exceeds 15000 points(present week) then make a csv on those observations as Exceeded expectations.csv
# 

# ###### if  10000<codekata score<15000   (Reached_expectations.csv)
# 
# 

# ###### if  7000<codekata score<10000   (Needs_Improvement.csv)
# 

# ###### if  codekate score < 7000        (Unsatisfactory.csv)

# In[70]:


EE = data[data["CodeKata Score"]>=15000]
RE1 = data[data["CodeKata Score"]<15000]
RE = RE1[RE1["CodeKata Score"]>=10000]
NI1 = data[data["CodeKata Score"]<10000]
NI = NI1[NI1["CodeKata Score"]>=7000]
UN = data[data["CodeKata Score"]<7000]


# In[71]:


EE.to_csv("Exceeded_Expectations.csv")
RE.to_csv("Reached_Expectations.csv")
NI.to_csv("Needs_Improvement.csv")
UN.to_csv("Unsatisfactory.csv")


# ###### Average of previous week geekions vs this week geekions (i.e Previous Geekions vs CodeKata Score)

# In[72]:


Ap=data["Previous Geekions"].mean()
print("The Average Previous Geekions is: ",Ap )


# In[73]:


Ac = data["CodeKata Score"].mean()
print("The Average This Week Geekions is: ",Ac)


# ###### No of students participated 

# In[74]:


data["Name"].nunique()


# ###### #Average completion of python course or my_sql or python english or computational thinking

# In[75]:


print("The Average Completion of python is:" ,data["python"].mean())
print("The Average Completion of python_en is:" ,data["python_en"].mean())
print("The Average Completion of mysql is:" ,data["mysql"].mean())
print("The Average Completion of computational thinking is:" ,data["computational_thinking"].mean())


# ###### rising star of the week (top 3 candidate who performed well in that particular week)

# In[76]:


data.sort_values("Rising", ascending=False).head(3)


# ###### Shining stars of the week (top 3 candidates who has highest geekions)

# In[77]:


data.sort_values("CodeKata Score", ascending=False).head(3)


# ###### Department wise codekata performence (pie chart)

# In[87]:


dt = data.groupby(["Department"])["CodeKata Score"].sum()
dt.plot(kind="pie")


# ###### Department wise toppers (horizantal bar graph or any visual representations of your choice)

# In[85]:


dep_top = data.groupby(["Department"])["Name","CodeKata Score"].max()
dep_top.plot(kind="barh", xlabel="CodeKata Score", color="skyblue")


# In[ ]:





# In[ ]:





# In[ ]:




