import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd 
from itertools import combinations 
from math import ceil 
import seaborn as sns
def updated_plot_hexbin_density(df, color='viridis'):
    numeric_df = df.select_dtypes(include=np.number)
    feat_pairs = list(combinations(numeric_df.columns, 2))  
    npairs = len(feat_pairs) 
    nrows = ceil(npairs/3) 
    figsize = (12, 4*nrows)  
    fig, axes = plt.subplots(ncols=3, nrows=nrows, figsize=figsize) 
    axes = axes.flatten()         
    for counter, (fi, fj) in enumerate(feat_pairs): 
        sns.hexbin(x=numeric_df[fi], y=numeric_df[fj], ax=axes[counter], cmap=color)
        axes[counter].set_title(f'{fi} vs {fj}') 
    for i in range(counter+1, len(axes)):        
        axes[i].set_visible(False)    
    fig.subplots_adjust(wspace=0.5, hspace=0.5)
    plt.tight_layout()
    plt.show()

df = pd.DataFrame({'x': [1, 2, 3, 4, 5], 'y': [5, 4, 3, 2, 1], 'z': ['a', 'b', 'c', 'd', 'e']})
updated_plot_hexbin_density(df, color='Blues')
