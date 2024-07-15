#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd 


# In[1]:


# Input : Unique_ID, Ra,Dec,Redshift, Group_ID 
def nmin_cut(result,nmin):
    result_copy = result.copy()
    
    uni_group = np.unique(result_copy[:,4])
    for idx,val in enumerate(uni_group):
        find = np.where(result_copy[:,4] == val)[0]
        if find.size < nmin:
            result_copy = np.delete(result_copy,find,axis=0)
    print("Total Number of Galaxies  :", len(result_copy[:,0]))
    print("Total Number of Finding Groups :", len(np.unique(result_copy[:,4])))
    return result_copy 


# In[ ]:


def group_summary(result):
    # fname,fra,fdec,fredshift,fnum
    uni_group = np.unique(result[:,4])
    gsum = np.zeros([5,len(uni_group)]).T
    
    
    for idx,val in enumerate(uni_group):
        find = np.where(result[:,4] == val)[0]
        
        
        f_ra = np.mean(result[:,1][find])
        f_dec = np.mean(result[:,2][find])
        f_redshift = np.mean(result[:,3][find])
        f_ID = val 
        f_num = len(find)
        
        gsum[idx] = np.array([f_ID,f_ra,f_dec,f_redshift,f_num])
    
    relabeling = np.arange(1,len(uni_group))
    
    nmin_col = gsum[:,4]
    
    sorted_indices = np.argsort(nmin_col)[::-1]
    sorted_gsum = gsum[sorted_indices]
    
    relabeling_gname = np.arange(1,len(nmin_col)+1)
    for idx,val in enumerate(relabeling_gname):
        sorted_gsum[:,0][idx] = val
    
    return sorted_gsum

