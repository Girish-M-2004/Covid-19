#!/usr/bin/env python
# coding: utf-8

# In[12]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


import plotly.io as pio
pio.renderers.default = 'colab'


# # Importing Datasets

# In[4]:


df = pd.read_csv("C:/covid.csv")
df.head()


# In[5]:


df1 = pd.read_csv("C:/covid_grouped.csv")
df1.head()


# In[6]:


df.columns


# # Cleaning the Data

# In[7]:


df.drop(['NewCases', 'NewDeaths', 'NewRecovered'],axis=1,inplace=True)
df.head()


# In[8]:


import plotly.offline as py
py.init_notebook_mode(connected = True)
import plotly.graph_objs as go
import plotly.express as px


# In[9]:


from plotly.figure_factory import create_table
table = create_table(df.head(10),colorscale='blues')
py.iplot(table)


# In[10]:


df.columns


# # Visualizing the Data

# Total Cases vs Country/Region

# In[11]:


px.bar(df.head(10), x='Country/Region', y='TotalCases', color='Country/Region', height=500, hover_data=['Country/Region', 'Continent'])


# Total Deaths vs Country/Region

# In[12]:


px.bar(df.head(10), x='Country/Region', y='TotalDeaths', color='Country/Region', height=500, hover_data=['Country/Region', 'Continent'])


# Total Recovered vs Country/Region

# In[13]:


px.bar(df.head(10), x='Country/Region', y='TotalRecovered', color='TotalRecovered', height=500, hover_data=['Country/Region', 'Continent'])


# Total Tests vs Country/Region

# In[14]:


px.bar(df.head(10), x='TotalTests', y='Country/Region', color='TotalTests', height=500, hover_data=['Country/Region', 'Continent'])


# # Continent wise Visualization

# Total Cases vs Continent

# In[15]:


px.scatter(df.head(50), x='Continent', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='TotalCases', size='TotalCases', size_max=80, log_y=True)


# Total Tests vs Continent

# In[16]:


px.scatter(df.head(50), x='Continent', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True)


# Total Deaths vs Continent

# In[17]:


px.scatter(df.head(50), x='Continent', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='TotalDeaths', size='TotalDeaths', size_max=80, log_y=True)


# Total Recovered vs Continent

# In[ ]:





# # Country wise Visualization 

# Total Cases vs Countries

# In[18]:


px.scatter(df.head(50), x='Country/Region', y='TotalCases', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalCases', size_max=80, log_y=True)


# Total Tests vs Countries

# In[19]:


px.scatter(df.head(50), x='Country/Region', y='TotalTests', hover_data=['Country/Region', 'Continent'], color='TotalTests', size='TotalTests', size_max=80, log_y=True)


# Total Deaths vs Countries

# In[20]:


px.scatter(df.head(50), x='Country/Region', y='TotalDeaths', hover_data=['Country/Region', 'Continent'], color='Country/Region', size='TotalDeaths', size_max=80, log_y=True)


# In[21]:


df1.columns


# Date vs Confirmed

# In[22]:


px.bar(df1, x='Date', y='Confirmed', color='Confirmed', hover_data=['Confirmed', 'Date', 'Country/Region'], log_y=True, height=400)


# Date vs Deaths

# In[23]:


px.bar(df1, x='Date', y='Deaths', color='Deaths', hover_data=['Deaths', 'Date', 'Country/Region'], log_y=False, height=400)


# # Analysis of United Kingdom

# In[24]:


df_uk = df1.loc[df1['Country/Region']=='United Kingdom']


# Date vs Confirmed (UK)

# In[25]:


px.bar(df_uk, x='Date', y='Confirmed', color='Confirmed', height=400)


# Date vs Deaths (UK)

# In[26]:


px.bar(df_uk, x='Date', y='Deaths', color='Deaths', height=400)


# # Analysis of India

# In[27]:


df_ind = df1.loc[df1['Country/Region']=='India']


# Date vs Confirmed (INDIA)

# In[28]:


px.line(df_ind, x='Date', y='Confirmed', height=400)


# Date vs Recovered (INDIA)

# In[29]:


px.line(df_ind, x='Date', y='Recovered', height=400)


# Date vs New Cases (INDIA)

# In[30]:


px.bar(df_ind, x='Date', y='New cases', color='New cases', height=400)


# Confirmed cases vs Deaths (INDIA)

# In[31]:


px.scatter(df_ind, x='Confirmed', y='Deaths', height=400, log_y=True)


# # Visualizing Data Using Maps

# In[32]:


px.choropleth(df1,
              locations='iso_alpha',
              color='Confirmed',
              hover_name='Country/Region',
              color_continuous_scale='reds',
              animation_frame='Date' )


# In[33]:


px.choropleth(df1,
              locations='iso_alpha',
              color='Deaths',
              hover_name='Country/Region',
              color_continuous_scale='blackbody',
              animation_frame='Date' )


# In[34]:


px.choropleth(df1,
              locations='iso_alpha',
              color='Confirmed',
              hover_name='Country/Region',
              color_continuous_scale='reds',
              projection='orthographic',
              animation_frame='Date' )


# In[35]:


px.choropleth(df1,
              locations='iso_alpha',
              color='Deaths',
              hover_name='Country/Region',
              color_continuous_scale='blackbody',
              projection='orthographic',
              animation_frame='Date' )


# In[36]:


px.choropleth(df1,
              locations='iso_alpha',
              color='Recovered',
              hover_name='Country/Region',
              color_continuous_scale='blues',
              projection='orthographic',
              animation_frame='Date' )


# # Reasons for deaths during Covid

# In[37]:


from wordcloud import WordCloud


# In[38]:


covid = pd.read_csv("C:/covid+death.csv")
covid.head()


# In[39]:


covid.tail()


# In[40]:


covid.groupby(['Condition']).count()


# In[41]:


covid.groupby(['Condition Group']).count()


# In[42]:


s_to_list = covid['Condition'].tolist()


# In[43]:


s_as_a_string = ' '.join(s_to_list)


# In[44]:


plt.figure(figsize=(15,15))
plt.imshow(WordCloud().generate(s_as_a_string))

