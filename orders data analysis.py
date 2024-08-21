#!/usr/bin/env python
# coding: utf-8

# In[23]:


#extract file from zip file
import zipfile
zip_ref = zipfile.ZipFile('orders.csv.zip') 
zip_ref.extractall() # extract file to dir
zip_ref.close() # close file

                    


# In[24]:


#read data from the file and handle null values
import pandas as pd
df = pd.read_csv('orders.csv',na_values=['Not Available','unknown'])
df['Ship Mode'].unique()


# In[34]:


#rename columns names ..make them lower case and replace space with underscore
#df.rename(columns={'Order Id':'order_id', 'City':'city'})
#df.columns=df.columns.str.lower()
#df.columns=df.columns.str.replace(' ','_')
df.head(5)




# In[37]:


#df['discount'] = df['list_price']*df['discount_percent']*.01
#df['sale_price'] = df['list_price']-df['discount']
df['profit'] = df['sale_price']-df['cost_price']
df


# In[44]:


#convert order date from object data type to datetime
#df.dtypes
df['order_date']=pd.to_datetime(df['order_date'],format="%Y-%m-%d")


# In[46]:


#drop cost price list price and discount percent columns
df.drop(columns=['list_price','cost_price','discount_percent'],inplace=True) # inplace=True means dropping it from our dataset (df)


# In[47]:


df


# In[51]:


pip install pyodbc


# In[52]:


#load the data into sql server using replace option
import sqlalchemy as sal
engine = sal.create_engine('mssql://DESKTOP-4HBM6FL\SQLEXPRESS/master?driver=ODBC+DRIVER+17+FOR+SQL+SERVER')
conn=engine.connect()


# In[57]:


#df.columns


# In[58]:


#load the data into sql server using append option
df.to_sql('df_orders', con=conn , index=False, if_exists = 'append') #df_orders would be table name, so instead of replace use append 
#else datatypes would come as bigint etc which will take more memory. also create table again in sql and then run this command using append.



