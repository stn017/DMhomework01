#!/usr/bin/env python
# coding: utf-8

# # Data Sources
# import data
# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
wine_reviews = pd.read_csv("./data/winemag-data-130k-v2.csv", index_col=0)
wine_reviews


# # Data Visualization and Summary
# Nominal type：
# country, designation, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery
# Numeric type:
# points, price# Nominal type：# country
# In[2]:


wine_reviews.groupby('country').country.count().sort_values()


# In[3]:


country_filter_reviews = wine_reviews.groupby('country').filter(lambda x: len(x) >= 2000)
country_reviews = country_filter_reviews.groupby('country').country.count().sort_values()
country_reviews.plot.bar()

# designation
# In[4]:


wine_reviews.groupby('designation').designation.count().sort_values()


# In[5]:


designation_filter_reviews = wine_reviews.groupby('designation').filter(lambda x: len(x) >= 300)
designation_reviews = designation_filter_reviews.groupby('designation').designation.count().sort_values()
designation_reviews.plot.bar()

# province
# In[6]:


wine_reviews.groupby('province').province.count().sort_values()


# In[7]:


province_filter_reviews = wine_reviews.groupby('province').filter(lambda x: len(x) >= 2000)
province_reviews = province_filter_reviews.groupby('province').province.count().sort_values()
province_reviews.plot.bar()

# region_1
# In[8]:


wine_reviews.groupby('region_1').region_1.count().sort_values()


# In[9]:


region_1_filter_reviews = wine_reviews.groupby('region_1').filter(lambda x: len(x) >= 1000)
region_1_reviews = region_1_filter_reviews.groupby('region_1').region_1.count().sort_values()
region_1_reviews.plot.bar()

# region_2
# In[10]:


wine_reviews.groupby('region_2').region_2.count().sort_values()


# In[11]:


region_2_filter_reviews = wine_reviews.groupby('region_2').filter(lambda x: len(x) >= 100)
region_2_reviews = region_2_filter_reviews.groupby('region_2').region_2.count().sort_values()
region_2_reviews.plot.bar()

# taster_name
# In[12]:


wine_reviews.groupby('taster_name').taster_name.count().sort_values()


# In[13]:


taster_name_filter_reviews = wine_reviews.groupby('taster_name').filter(lambda x: len(x) >= 6)
taster_name_reviews = taster_name_filter_reviews.groupby('taster_name').taster_name.count().sort_values()
taster_name_reviews.plot.bar()

# taster_twitter_handle
# In[14]:


wine_reviews.groupby('taster_twitter_handle').taster_twitter_handle.count().sort_values()


# In[15]:


taster_twitter_handle_filter_reviews = wine_reviews.groupby('taster_twitter_handle').filter(lambda x: len(x) >= 6)
taster_twitter_handle_reviews = taster_twitter_handle_filter_reviews.groupby('taster_twitter_handle').taster_twitter_handle.count().sort_values()
taster_twitter_handle_reviews.plot.bar()

# title
# In[16]:


wine_reviews.groupby('title').title.count().sort_values()


# In[17]:


title_filter_reviews = wine_reviews.groupby('title').filter(lambda x: len(x) >= 6)
title_reviews = title_filter_reviews.groupby('title').title.count().sort_values()
title_reviews.plot.bar()

# variety
# In[18]:


wine_reviews.groupby('variety').variety.count().sort_values()


# In[19]:


variety_filter_reviews = wine_reviews.groupby('variety').filter(lambda x: len(x) >= 2000)
variety_reviews = variety_filter_reviews.groupby('variety').variety.count().sort_values()
variety_reviews.plot.bar()

# winery
# In[20]:


wine_reviews.groupby('winery').winery.count().sort_values()


# In[21]:


winery_filter_reviews = wine_reviews.groupby('winery').filter(lambda x: len(x) >= 120)
winery_reviews = winery_filter_reviews.groupby('winery').winery.count().sort_values()
winery_reviews.plot.bar()

# Numeric type:# points
# In[22]:


np.percentile(wine_reviews.points, (25, 50, 75))


# In[23]:


wine_reviews.points.isnull().sum()


# In[24]:


plt.boxplot(wine_reviews.points)

# price
# In[25]:


wine_reviews.price.mean()


# In[26]:


np.percentile(wine_reviews.loc[wine_reviews.price >= 0 ].price, (25, 50, 75))


# In[27]:


wine_reviews.price.isnull().sum()


# In[28]:


plt.boxplot(wine_reviews.loc[wine_reviews.price >= 0 ].price)


# # Dealing with Missing Data
# Missing Data: price
# Some of the wine maybe too old to find the exactly price or have no standard price.# Remove missing parts
# In[29]:


wine_reviews_deal1 = wine_reviews[wine_reviews['price'].notna()]
wine_reviews_deal1


# In[30]:


plt.boxplot(wine_reviews_deal1.price)

# Fill the missing value with the highest frequency value
# In[31]:


wine_reviews_deal2 = wine_reviews
ser_deal2 = pd.Series(wine_reviews_deal1['price'])
wine_reviews_deal2['price'] = wine_reviews_deal2['price'].fillna(ser_deal2.mode()[0]) 
wine_reviews_deal2


# In[32]:


plt.boxplot(wine_reviews_deal2.price)

# Fill missing values through correlation of attributes
# In[33]:


from sklearn import linear_model
X = pd.DataFrame(wine_reviews_deal1['points'])
y = wine_reviews_deal1['price']
clf = linear_model.LinearRegression()
clf.fit(X, y)
wine_reviews_deal3 = wine_reviews
for index in range(len(wine_reviews_deal3['points'])):
 if np.isnan(wine_reviews_deal3['price'][index]) : wine_reviews_deal3['price'][index] = clf.coef_ * wine_reviews_deal3['points'][index]  
wine_reviews_deal3


# In[34]:


plt.boxplot(wine_reviews_deal3.price)

# Fill missing values through similarity between data objects
# In[35]:


wine_reviews_deal4 = wine_reviews
wine_reviews_deal4['price'] = wine_reviews_deal4['price'].fillna(method='bfill') 
wine_reviews_deal4


# In[36]:


plt.boxplot(wine_reviews_deal4.price)

