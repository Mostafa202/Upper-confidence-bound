import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import sys

dataset=pd.read_csv('Ads_CTR_Optimisation.csv')


d=dataset.shape[1]
ads_selected=[]
number_of_selections=[0]*d
sum_of_rewards=[0]*d


for i in range(len(dataset)):
    max_upper=0
    ad=0
    for j in range(d):
        if number_of_selections[j] > 0:
            avg_reward=sum_of_rewards[j]/number_of_selections[j]
            delta_i=math.sqrt((3/2)*(math.log(i)/number_of_selections[j]))
            upper_bound=delta_i + avg_reward
        else:
            upper_bound=sys.maxsize
            
        if upper_bound>max_upper:
            max_upper=upper_bound
            ad=j
    ads_selected.append(ad)
    number_of_selections[ad]+=1
    reward=dataset.iloc[i,ad]
    sum_of_rewards[ad]+=reward
    
plt.hist(ads_selected)
plt.xlabel('ads')
plt.ylabel('the rate of ads')

            






