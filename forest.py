#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install openpyxl')
import pandas as pd
import seaborn as sns
import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px


# ### *Importing our shape file and our data*

# In[4]:


df = pd.read_excel('Forest.xlsx')
shp_gdf = gpd.read_file('states/Indian_states.shp')


# In[5]:


df.head(40)


# ### *Renaming the states in our dataset to match the shape file*

# In[6]:


df1 = df[['State/UTs', 'Percentage of geographical area']]
df1['State/UTs'][30] = 'Andaman & Nicobar Island'
df1['State/UTs'][1] = 'Arunanchal Pradesh'
df1['State/UTs'][32] = 'Dadara & Nagar Havelli'
df1['State/UTs'][5] = 'NCT of Delhi'


# In[7]:


merged = shp_gdf.set_index('st_nm').join(df1.set_index('State/UTs'))
merged.head(40)


# In[8]:


fig, ax = plt.subplots(1, figsize=(12, 12))
ax.axis('off')
ax.set_title('Percentage of Forest Coverage as of 2019',
             fontdict={'fontsize': '20', 'fontweight' : '5'})
fig = merged.plot(column='Percentage of geographical area', cmap='Greens', linewidth=0.5, ax=ax, edgecolor='0.1',legend=True)


# In[9]:


plt.figure(figsize=(15,8))
sns.barplot(x="Percentage of geographical area", y = "State/UTs", data = df1)

