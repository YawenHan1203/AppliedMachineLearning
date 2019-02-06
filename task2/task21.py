import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
%matplotlib inline
#load dataset
df=pd.read_csv("ScienceCorSuicides.csv")

fig=plt.figure(figsize=(8, 6))
#plots
ax1 = plt.gca()
line1, = ax1.plot(df["year"], df["suicides"],c="r",marker="D")
ax2 = ax1.twinx()
line2, = ax2.plot(df["year"], df["spending"], c="k",marker="o")
#set label
ax1.set_ylabel("US spending on science") 
ax2.set_ylabel("Hanging suicides",rotation=270)
#legend
ax2.legend((line1, line2),("US spending on science", "Hanging suicides"),loc="upper left")
#set xticks
_=plt.xticks(np.arange(1999,2010))
_=ax1.xaxis.set_tick_params(top=True,labeltop='on')
#set limits
_=ax1.set_ylim(15,30)
_=ax2.set_ylim(4000,10000)
#set yticks
_=ax1.set_yticks([15,20,25,30])
_=ax2.set_yticks([4000,6000,8000,10000])
_=ax1.set_yticklabels(['$15 billion','$20 billion','$25 billion','$30 billion'])
_=ax2.set_yticklabels(['4000 suicides','6000 suicides','8000 suicides','10000 suicides'])
#add title
_=fig.suptitle("US spending on science, space, and technology\n correlates with\n Suicides by hanging, strangulation and duffocation", fontsize=14, fontweight='bold')
_=fig.subplots_adjust(top=0.78)
_=ax1.set_title('Correlation: 99.79% (r=0.99789126)',pad=25)
_=plt.grid()
plt.show()
