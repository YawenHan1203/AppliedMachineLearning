from sklearn.datasets import load_iris 
import matplotlib.pyplot as plt 
import numpy as np
%matplotlib inline
#load data
iris_dataset = load_iris()
X = iris_dataset.data
Y = iris_dataset.target

fig, ax = plt.subplots(4,4,figsize=(10,10))
#delete space between subplots
fig.subplots_adjust(wspace=0, hspace=0)
#set matrix plot
for i,row in enumerate(iris_dataset.feature_names):
    for j,column in enumerate(iris_dataset.feature_names):
        #scatter plots
        if i != j:
            scatter=ax[i,j].scatter(X[:,j],X[:,i],c=Y, cmap='rainbow', edgecolor='k', alpha=0.8)   
        else:
        #histogram
            ax[i,j].hist(X[:,j],color='blue',edgecolor='black',bins=20)
        #set label
        ax[i,0].set_ylabel(row)
        ax[3,j].set_xlabel(column)
        #set ticks
        if j!=0:
            ax[i,j].tick_params(left=False,labelleft=False)
        ax[0,0].tick_params(labelcolor='white',pad=-2)
        ax[0,1].tick_params(labelleft=True,pad=145)
        ax[2,0].tick_params(labelleft=True,pad=12)
             
#set legend
labels =iris_dataset.target_names
handles = [plt.Line2D([],[],marker="o",ls="",color=scatter.cmap(scatter.norm(yi))) for yi in np.unique(Y)]
_=fig.legend(handles, labels,loc='right')
#set title
_=fig.suptitle("Iris data matrix plots",fontsize=14, fontweight='bold')
_=fig.subplots_adjust(top=0.93)
plt.show()