#!/usr/bin/env python
# coding: utf-8

# In[76]:


# Python Project 2
### Question : What is the difference between peoples's race and gender with diabetes? Who is at a higher risk?

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

get_ipython().run_line_magic('matplotlib', 'inline')

df = pd.read_csv(r'Desktop/Data_analysis/NYPD_Hate_Crimes .csv')
df
df.head()
df.shape
df.describe()

###changing the index to encounter_id 
#check first if the ID is unique 
df['Full Complaint ID'].is_unique 
#it is true 

df = df.set_index('Full Complaint ID')

##

#Dropping Columns that are not needed/has NaN values 
drop_list = ['Other Motive Description','Arrest Date','Arrest Id']
df.drop(drop_list, inplace=True, axis=1)
df


# In[77]:


df.groupby(['Complaint Year Number'])['PD Code Description'].count() #more women have diabetes 54708 Women & 47055 Men

df.groupby(['Offense Category'])['County'].count()


# In[78]:


sns.countplot(y='County', hue='Offense Category', data=df, palette="Greens_d")


# In[83]:


options = ['race/color'] 
    
# selecting rows based on condition 
df = df[(df['Complaint Year Number'] == 2020) & 
          df['Offense Category'].isin(options)] 
    
print('\nResult dataframe :\n',
      df)


# In[95]:


df2 = pd.DataFrame(np.random.rand(20, 4), columns=["Complaint Year Number", "County", "Offense Description", "Offense Category"])

df2.plot.bar();


# In[ ]:




