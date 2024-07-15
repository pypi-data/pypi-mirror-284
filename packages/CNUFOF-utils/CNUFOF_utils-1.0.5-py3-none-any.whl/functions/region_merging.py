#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from tqdm import trange

# In[1]:
def renew_region_merging(parallel_field1,parallel_field2):
    final_group1 = np.zeros(len(parallel_field1[:,4]))
    final_group2 = np.zeros(len(parallel_field2[:,4]))
    
    parallel_field1_copy = parallel_field1.copy()
    parallel_field2_copy = parallel_field2.copy()
    
    
    grid1 = parallel_field1[:,4].copy()
    grid2 = parallel_field2[:,4].copy()
    
    com_part,paral1_com_part_idx,paral2_com_part_idx = np.intersect1d(parallel_field1[:,0],parallel_field2[:,0],return_indices=True)
    
    for i in range(len(paral1_com_part_idx)):
        if (grid1[paral1_com_part_idx[i]] == grid2[paral2_com_part_idx[i]]):
            continue
        ind1 = np.where(grid1 == grid1[paral1_com_part_idx[i]])[0]
        ind2 = np.where(grid2 == grid2[paral2_com_part_idx[i]])[0]
        if (any(final_group1[ind1] ==0)|any(final_group2[ind2] ==0)):
            tmpid = grid1[paral1_com_part_idx[i]]
        else:
            tmpid = final_group1[paral1_com_part_idx[i]]
        find_revision_group = np.where(grid1 == grid2[paral2_com_part_idx[i]])[0]
        
        grid1[ind1] = tmpid
        grid2[ind2] = tmpid
        grid1[find_revision_group] = tmpid
        final_group1[ind1] = tmpid
        final_group2[ind2] = tmpid 
        final_group1[find_revision_group] = tmpid
        
    parallel_field1_copy[:,4] = grid1
    parallel_field2_copy[:,4] = grid2
    
    
    parallel_field1_copy = np.concatenate((parallel_field1_copy,parallel_field2_copy))
    parallel_field1_copy = np.flip(parallel_field1_copy,axis=0)
    
    tot_idx = np.unique(parallel_field1_copy[:,0],return_index= True )[1]
    
    return parallel_field1_copy[tot_idx]



# In[ ]:

def Total_merging(parallel_result):
    result= renew_region_merging(parallel_result[0],parallel_result[1])
    for i in range(1,len(parallel_result)-1):
        result = renew_region_merging(result,parallel_result[i+1])
    return result

def nmin_unique(fields):
    lst = np.array([])
    for idx,val in enumerate(np.unique(fields[:,4])):
        find = np.where(fields[:,4] == val)[0].astype(int)
        if find.size <= 4 :
            fields = np.delete(fields,find,axis=0)
    return fields 

