import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

#load dataset
df_mpg=pd.read_csv("mpg.csv",index_col=0)

fig, ax = plt.subplots(2,2,figsize=(10,10))
#preprocess data
df_mpg["drv"][df_mpg["drv"]=='f'] = 'FWD'
df_mpg["drv"][df_mpg["drv"]=='r'] = 'RWD'
df_mpg["drv"][df_mpg["drv"]=='4'] = '4WD'

#first plot
colors = ['black','orange','blue']
drv = np.unique(df_mpg["drv"])
for i in range(len(drv)):
    data = df_mpg.loc[df_mpg["drv"] == drv[i]]
    _=ax[0,0].scatter(data["displ"],data["cty"], color=colors[i], label=drv[i])
_=ax[0,0].legend(title="drive train",edgecolor="white")
_=ax[0,0].set_ylabel("fuel economy (mpg)")
_=ax[0,0].set_xlabel("displacement (l)")
_=ax[0,0].set_title("Figure 18.1")

#second plot
for i in range(len(drv)):
    data = df_mpg.loc[df_mpg["drv"] == drv[i]]
    _=ax[0,1].scatter(data["displ"],data["cty"], color=colors[i], label=drv[i],alpha=0.5)
_=ax[0,1].legend(title="drive train",edgecolor="white")
_=ax[0,1].set_ylabel("fuel economy (mpg)")
_=ax[0,1].set_xlabel("displacement (l)")
_=ax[0,1].set_title("Figure 18.2")

#third plot
#random jitter function
def rand_jitter(arr):
    stdev = .01*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev

for i in range(len(drv)):
    data = df_mpg.loc[df_mpg["drv"] == drv[i]]
    _=ax[1,0].scatter(rand_jitter(data["displ"]),rand_jitter(data["cty"]), color=colors[i], label=drv[i],alpha=0.5)
_=ax[1,0].legend(title="drive train",edgecolor="white")
_=ax[1,0].set_ylabel("fuel economy (mpg)")
_=ax[1,0].set_xlabel("displacement (l)")
_=ax[1,0].set_title("Figure 18.3")


#third plot
#over jitter function
def over_jitter(arr):
    stdev = .1*(max(arr)-min(arr))
    return arr + np.random.randn(len(arr)) * stdev
for i in range(len(drv)):
    data = df_mpg.loc[df_mpg["drv"] == drv[i]]
    _=ax[1,1].scatter(over_jitter(data["displ"]),over_jitter(data["cty"]), color=colors[i], label=drv[i],alpha=0.5)
_=ax[1,1].legend(title="drive train",edgecolor="white")
_=ax[1,1].set_ylabel("fuel economy (mpg)")
_=ax[1,1].set_xlabel("displacement (l)")
_=ax[1,1].set_title("Figure 18.4")

#suptitle
_=fig.suptitle("City fuel economy vs. engine displacement,1999-2008",fontsize=14, fontweight='bold')
_=fig.subplots_adjust(top=0.93)


