#!/usr/bin/env python
# coding: utf-8

# # Data Sources
# import data
# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
bv_reviews = pd.read_csv("./data/building-violations.csv")
bv_reviews


# # Data Visualization and Summary
# Nominal type：
# VIOLATION CODE, VIOLATION DESCRIPTION, VIOLATION LOCATION, INSPECTOR ID, INSPECTION STATUS, INSPECTION CATEGORY, DEPARTMENT BUREAU, STREET DIRECTION, STREET TYPE, Community Areas, Zip Codes, Boundaries - ZIP Codes, Census Tracts, Wards, Historical Wards 2003-2015

# Numeric type:
# LATITUDE, LONGITUDE# Nominal type：# VIOLATION CODE
# In[2]:


bv_reviews.groupby('VIOLATION CODE').ID.count().sort_values()


# In[3]:


VC_filter_reviews = bv_reviews.groupby('VIOLATION CODE').filter(lambda x: len(x) >= 25000)
VC_reviews = VC_filter_reviews.groupby('VIOLATION CODE').ID.count().sort_values()
VC_reviews.plot.bar()

# VIOLATION DESCRIPTION
# In[4]:


bv_reviews.groupby('VIOLATION DESCRIPTION').ID.count().sort_values()


# In[5]:


VD_filter_reviews = bv_reviews.groupby('VIOLATION DESCRIPTION').filter(lambda x: len(x) >= 25000)
VD_reviews = VD_filter_reviews.groupby('VIOLATION DESCRIPTION').ID.count().sort_values()
VD_reviews.plot.bar()

# VIOLATION LOCATION
# In[6]:


bv_reviews.groupby('VIOLATION LOCATION').ID.count().sort_values()


# In[7]:


VL_filter_reviews = bv_reviews.groupby('VIOLATION LOCATION').filter(lambda x: len(x) >= 10000)
VL_reviews = VL_filter_reviews.groupby('VIOLATION LOCATION').ID.count().sort_values()
VL_reviews.plot.bar()

# INSPECTOR ID
# In[8]:


bv_reviews.groupby('INSPECTOR ID').ID.count().sort_values()


# In[9]:


IID_filter_reviews = bv_reviews.groupby('INSPECTOR ID').filter(lambda x: len(x) >= 15000)
IID_reviews = IID_filter_reviews.groupby('INSPECTOR ID').ID.count().sort_values()
IID_reviews.plot.bar()

# INSPECTION STATUS
# In[10]:


bv_reviews.groupby('INSPECTION STATUS').ID.count().sort_values()


# In[11]:


IS_filter_reviews = bv_reviews.groupby('INSPECTION STATUS').filter(lambda x: len(x) >= 100)
IS_reviews = IS_filter_reviews.groupby('INSPECTION STATUS').ID.count().sort_values()
IS_reviews.plot.bar()

# INSPECTION CATEGORY
# In[12]:


bv_reviews.groupby('INSPECTION CATEGORY').ID.count().sort_values()


# In[13]:


IC_filter_reviews = bv_reviews.groupby('INSPECTION CATEGORY').filter(lambda x: len(x) >= 2000)
IC_reviews = IC_filter_reviews.groupby('INSPECTION CATEGORY').ID.count().sort_values()
IC_reviews.plot.bar()

# DEPARTMENT BUREAU
# In[14]:


bv_reviews.groupby('DEPARTMENT BUREAU').ID.count().sort_values()


# In[15]:


DB_filter_reviews = bv_reviews.groupby('DEPARTMENT BUREAU').filter(lambda x: len(x) >= 120)
DB_reviews = DB_filter_reviews.groupby('DEPARTMENT BUREAU').ID.count().sort_values()
DB_reviews.plot.bar()

# STREET DIRECTION
# In[16]:


bv_reviews.groupby('STREET DIRECTION').ID.count().sort_values()


# In[17]:


SD_filter_reviews = bv_reviews.groupby('STREET DIRECTION').filter(lambda x: len(x) >= 120)
SD_reviews = SD_filter_reviews.groupby('STREET DIRECTION').ID.count().sort_values()
SD_reviews.plot.bar()

# STREET TYPE
# In[18]:


bv_reviews.groupby('STREET TYPE').ID.count().sort_values()


# In[19]:


ST_filter_reviews = bv_reviews.groupby('STREET TYPE').filter(lambda x: len(x) >= 3)
ST_reviews = ST_filter_reviews.groupby('STREET TYPE').ID.count().sort_values()
ST_reviews.plot.bar()

# Community Areas
# In[20]:


bv_reviews.groupby('Community Areas').ID.count().sort_values()


# In[21]:


CA_filter_reviews = bv_reviews.groupby('Community Areas').filter(lambda x: len(x) >= 25000)
CA_reviews = CA_filter_reviews.groupby('Community Areas').ID.count().sort_values()
CA_reviews.plot.bar()

# Zip Codes
# In[22]:


bv_reviews.groupby('Zip Codes').ID.count().sort_values()


# In[23]:


ZC_filter_reviews = bv_reviews.groupby('Zip Codes').filter(lambda x: len(x) >= 20000)
ZC_reviews = ZC_filter_reviews.groupby('Zip Codes').ID.count().sort_values()
ZC_reviews.plot.bar()

# Boundaries - ZIP Codes
# In[24]:


bv_reviews.groupby('Boundaries - ZIP Codes').ID.count().sort_values()


# In[25]:


BZC_filter_reviews = bv_reviews.groupby('Boundaries - ZIP Codes').filter(lambda x: len(x) >= 20000)
BZC_reviews = BZC_filter_reviews.groupby('Boundaries - ZIP Codes').ID.count().sort_values()
BZC_reviews.plot.bar()

# Census Tracts
# In[26]:


bv_reviews.groupby('Census Tracts').ID.count().sort_values()


# In[27]:


CTS_filter_reviews = bv_reviews.groupby('Census Tracts').filter(lambda x: len(x) >= 2000)
CTS_reviews = CTS_filter_reviews.groupby('Census Tracts').ID.count().sort_values()
CTS_reviews.plot.bar()

# Wards
# In[28]:


bv_reviews.groupby('Wards').ID.count().sort_values()


# In[29]:


Wards_filter_reviews = bv_reviews.groupby('Wards').filter(lambda x: len(x) >= 2000)
Wards_reviews = Wards_filter_reviews.groupby('Wards').ID.count().sort_values()
Wards_reviews.plot.bar()

# Historical Wards 2003-2015
# In[30]:


bv_reviews.groupby('Historical Wards 2003-2015').ID.count().sort_values()


# In[31]:


HisWards_filter_reviews = bv_reviews.groupby('Historical Wards 2003-2015').filter(lambda x: len(x) >= 2000)
HisWards_reviews = HisWards_filter_reviews.groupby('Historical Wards 2003-2015').ID.count().sort_values()
HisWards_reviews.plot.bar()

# Numeric type:# LATITUDE
# In[32]:


np.percentile(bv_reviews.loc[bv_reviews.LATITUDE >= min(bv_reviews.LATITUDE)].LATITUDE, (25, 50, 75))


# In[33]:


bv_reviews.LATITUDE.isnull().sum()


# In[34]:


plt.boxplot(bv_reviews.loc[bv_reviews.LATITUDE >= min(bv_reviews.LATITUDE)].LATITUDE)

# LONGITUDE
# In[35]:


np.percentile(bv_reviews.loc[bv_reviews.LONGITUDE >= min(bv_reviews.LONGITUDE)].LONGITUDE, (25, 50, 75))


# In[36]:


bv_reviews.LONGITUDE.isnull().sum()


# In[37]:


plt.boxplot(bv_reviews.loc[bv_reviews.LONGITUDE >= min(bv_reviews.LONGITUDE)].LONGITUDE)


# # Dealing with Missing Data
# Missing Data: price
# Some of the wine maybe too old to find the exactly price or have no standard price.# Remove missing parts
# In[38]:


bv_reviews_deal1 = bv_reviews[bv_reviews['LATITUDE'].notna()]
bv_reviews_deal1


# In[39]:


plt.boxplot(bv_reviews_deal1.LATITUDE)


# In[40]:


plt.boxplot(bv_reviews_deal1.LONGITUDE)

# Fill the missing value with the highest frequency value
# In[41]:


bv_reviews_deal2 = bv_reviews
ser1_deal2 = pd.Series(bv_reviews_deal1['LATITUDE'])
ser2_deal2 = pd.Series(bv_reviews_deal1['LONGITUDE'])
bv_reviews_deal2['LATITUDE'] = bv_reviews_deal2['LATITUDE'].fillna(ser1_deal2.mode()[0]) 
bv_reviews_deal2['LONGITUDE'] = bv_reviews_deal2['LONGITUDE'].fillna(ser2_deal2.mode()[0])
bv_reviews_deal2


# In[42]:


plt.boxplot(bv_reviews_deal2.LATITUDE)


# In[43]:


plt.boxplot(bv_reviews_deal2.LONGITUDE)

# Fill missing values through similarity between data objects
# In[44]:


bv_reviews_deal3 = bv_reviews
bv_reviews_deal3['LATITUDE'] = bv_reviews_deal3['LATITUDE'].fillna(method='bfill') 
bv_reviews_deal3['LONGITUDE'] = bv_reviews_deal3['LONGITUDE'].fillna(method='bfill') 
bv_reviews_deal3


# In[45]:


plt.boxplot(bv_reviews_deal3.LATITUDE)


# In[46]:


plt.boxplot(bv_reviews_deal3.LONGITUDE)

