import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#creating a dataframe from random number and creating a plot of it
# np.random.seed(20)
# df = pd.DataFrame(np.random.rand(10,1) , index=pd.date_range('2022-06-21' , periods=10), columns=['data'])
# df.data.cumsum().plot()
# df['data_cumsum'] = df1.data.cumsum()
# df['datasq'] = df1['data'].apply(lambda x : x **2)
# df.plot(figsize=(12,12))
# plt.show()
#
# #loading Iris Data Set into dataframe and displaying it on plot
#
# df1= pd.DataFrame(sns.load_dataset('iris'))
# #in case we need to plot bar garph we can create using kind parameters
# #title will give name to the graph
# gf= df1.plot(figsize=(10,10), title = "Iris data",kind='bar')
# #it will set xlable of the graph
# gf.set_xlabel("X-Axis")
# #it will set ylabel of the Grapb
# gf.set_ylabel("Y-Axis")

# plt.show()



#loading Titanic  Data Set into dataframe and displaying it on plot

df1= pd.DataFrame(sns.load_dataset('titanic'))
#in case we need to plot bar garph we can create using kind parameters
#title will give name to the graph
gf= df1.plot(figsize=(10,10), title = "titanic data",)
#it will set xlable of the graph
gf.set_xlabel("X-Axis")
#it will set ylabel of the Grapb
gf.set_ylabel("Y-Axis")
plt.show()
