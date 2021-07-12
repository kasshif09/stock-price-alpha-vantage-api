#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd
import matplotlib.pyplot as plt
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.sectorperformance import SectorPerformances
import seaborn as sns
from alpha_vantage.techindicators import TechIndicators

#Timeseries for timeseries stock data
#sector performance for US sector Performances
#tech indicators for technical indicators


# In[4]:


#use alpha vantage API key
key = 'ID101UMV4566KQI9'


# In[9]:


#stock market performance by sector
sp = SectorPerformances(key, output_format = 'pandas')
sector, meta_data = sp.get_sector()
sector.head()


# In[12]:


sector['Rank G: Year Performance'].plot(kind='bar')
plt.title("Performance by sector")
plt.tight_layout()
plt.grid(True)
#strong performance in financials sector


# In[36]:


#is PYPL worth investing in? lets see it stock price
symbol = 'PYPL'

ts = TimeSeries(key, output_format = 'pandas')
daily, meta = ts.get_daily('PYPL', outputsize= 'full')

columns = ['open', 'high','low', 'close', 'volume']
daily.columns = columns
daily['TradeDate'] = data.index.date
#daily['time'] = data.index.time
daily.head()


# In[35]:


#PYPL Single Moving Average Price (SMA)
ta = TechIndicators(key, output_format = 'pandas')
sma, meta = ta.get_sma('PYPL', interval = 'daily', time_period = 200, series_type='close')


# In[62]:


#PYPL combining SMA and closing price time series
sns.set(rc={'figure.figsize':(8,6)})
plt.plot(daily['close'])
plt.plot(sma)
plt.xlabel("Years", labelpad=12)
plt.ylabel("Closing Price", labelpad=10)
plt.title('$'+symbol, y=1.02, fontweight = 'bold', fontsize = 14);


# In[63]:


#Company overview API
import requests
import json

call = requests.get(f'https://www.alphavantage.co/query?function=OVERVIEW&symbol={symbol}&apikey={key}').text


# In[64]:


call = json.loads(call)
call = pd.DataFrame.from_dict(call, orient= 'index')
call


# In[205]:


#Earnings API
symbol = 'PYPL'
function = 'EARNINGS'

call2 = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}').text

call2 = json.loads(call2)
#call2


# In[176]:


#EPS comparison over the years
ae=pd.DataFrame(call2['annualEarnings'])


ae["reportedEPS"] = pd.to_numeric(ae["reportedEPS"], downcast="float")
pd.to_datetime(ae['fiscalDateEnding'])
ae.set_index('fiscalDateEnding', inplace=True)

ae.sort_values(by='fiscalDateEnding',axis=0, ascending=True, inplace=False)

ae


# In[203]:


#increasing EPS over the years
sns.set(rc={'figure.figsize':(8,6)})

ae[1:].plot.bar(color = 'tab:red').invert_xaxis()
plt.xlabel("Years", labelpad=12)
plt.ylabel("Earnings Per Share ($USD)", labelpad=10)
plt.title('$'+symbol, y=1.02, fontweight = 'bold', fontsize = 14);


# In[234]:


#Income Statement API
function = 'INCOME_STATEMENT'

call3 = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}').text

call3 = json.loads(call3)
#call3


# In[218]:


#gross profit and revenue time series
ar=pd.DataFrame(call3['annualReports'])


#ae["reportedEPS"] = pd.to_numeric(ae["reportedEPS"], downcast="float")
pd.to_datetime(ar['fiscalDateEnding'])
ar.set_index('fiscalDateEnding', inplace=True)
ar["grossProfit"] = pd.to_numeric(ar["grossProfit"], downcast="integer")

#ae.sort_values(by='fiscalDateEnding',axis=0, ascending=False, inplace=False)

ar


# In[232]:


sns.set(rc={'figure.figsize':(8,6)})

ar['grossProfit'].plot.bar(color = 'tab:blue').invert_xaxis()
plt.xlabel("Years", labelpad=12)
plt.ylabel("Gross Profit ($USD)", labelpad=10)
plt.title('$'+ symbol + 'Gross Profit Over the Last 5 Years', y=1.02, fontweight = 'bold', fontsize = 14); 


# In[237]:


#Balance sheet API
function = 'BALANCE_SHEET'

call4 = requests.get(f'https://www.alphavantage.co/query?function={function}&symbol={symbol}&apikey={key}').text

call4 = json.loads(call4)
call4


# In[ ]:





# In[ ]:





# In[243]:


from pygooglenews import GoogleNews

gn = GoogleNews()
top = gn.top_news()


# In[245]:


search = gn.search('PYPL', when = '6m')
search


# In[ ]:




