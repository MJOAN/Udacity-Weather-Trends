#%% [markdown]
# ## Explore Weather Trends 
# #### 1. Create a `line chart` that compares your `city’s temperatures` with the `global temperatures` and `plot` the `moving average` rather than the yearly averages in order to `smooth out` the lines, making trends more observable 
# #### 2. Make `observations` about the similarities and `differences` between the `world averages` and your `city’s averages`, as well as `overall trends`. 
# ##### a. Is your city hotter or cooler on average compared to the global average? Has the difference been consistent over time?
# ##### b. “How do the changes in your city’s temperatures over time compare to the changes in the global average?”
# ##### c. What does the overall trend look like? Is the world getting hotter or cooler? Has the trend been consistent over the last few hundred years?

#%%
import pandas as pd
from IPython.display import HTML
from IPython.core.interactiveshell import InteractiveShell  
InteractiveShell.ast_node_interactivity = "all"
from matplotlib import style, figure
 
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.style.use('ggplot')

city_data = pd.read_csv('city_data.csv')
global_data = pd.read_csv('global_data.csv')


#%%
global_data.drop(global_data.head(99).index,inplace=True) # drop last n rows
global_data.drop(global_data.tail(2).index,inplace=True) # drop last n rows
global_data.shape


#%%
city_data.shape


#%%
city_year = city_data['year']
global_year = global_data['year']
city_temp = city_data['avg_temp']
global_temp = global_data['avg_temp']

print('city: ', city_year.tail(), 'global: ', global_year.tail())


#%%
print('city: ', city_temp.tail(), 'global: ', global_temp.tail())


#%%
city_temp, global_temp


#%%
plt.plot(city_year, city_temp.rolling(window=30).mean(), 'r-', label='city: 30 MA')
plt.plot(global_year, global_temp.rolling(window=30).mean(), 'g-', label='global: 30 MA')
plt.legend(loc='best')

plt.xlabel('year')
plt.ylabel('average temperature C°')
plt.title('exploring global & local (los angeles, ca) weather trends')

style.use('ggplot')
plt.plot(figsize=(40,20))
print(plt.style.available)
plt.show()

#cite: https://towardsdatascience.com/implementing-moving-averages-in-python-1ad28e636f9d


#%%



#%%



#%%



#%%



#%%



#%%



