#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import astropy.cosmology 
from functools import partial 
import os
import astropy.units as u
import pandas as pd
import glob
import matplotlib.pyplot as plt
from astropy.cosmology import FlatLambdaCDM , Planck18
import time
from tqdm import trange
from pydl.goddard.astro import gcirc
import astropy.units as u
import ray
import sys
sys.setrecursionlimit(10**6)


# depth 설정 


# In[ ]:


class fofradecV():
    def __init__(self,h0c,omegamc,omegalc,omegakc,c,sdcondc,vcondc): 
        self.h0c = h0c 
        self.omegamc = omegamc
        self.omegalc = omegalc
        self.omegakc = omegakc
        self.c = c 
        self.sdcondc = sdcondc
        self.vcondc = vcondc
    
    
    def solution(self,i1,k,flag,lst,ra,de,v):
        """
        Descendant Node(s)
        """
        rax = ra[i1]
        dex = de[i1]
        vx = v[i1]
        # 전체에 대한 flag != 1 index 
        range1 = np.where(flag != 1)[0]
        cnt = range1.size 
        if (cnt >= 1):
            
            d12 = gcirc(rax/15,dex,ra[range1]/15,de[range1],1) # 상위 집합  range1
            sdcond1 = self.sdcondc[i1] 
            v12 = abs((vx-v[range1])/(1.+vx/self.c))
            v21 = abs((vx-v[range1])/(1+v[range1]/self.c))
            
            v_idx = np.where((v12<=self.vcondc)|(v21<=self.vcondc))[0]             # 상위 집합 range1 -> v_idx
            
           
            d_idx = np.where((d12[v_idx]<=sdcond1)|(d12[v_idx]<=self.sdcondc[range1[v_idx]]))[0] # range1 -> v_idx -> d_idx
            
            grj = v_idx[d_idx]

            num = grj.size                
            if (num == 0):pass

            if (num == 1):  
                lst[k+1] = range1[grj]
                flag[range1[grj]] = 1
                k += 1 
                
            if (num > 1):
                lst[k+1:k+num+1] = range1[grj]
                flag[range1[grj]] = 1
                k+= num
                
            for j in range(0,num):
                """
                Recrusive Function
                """
                alpha = range1[grj[j]]
                lst,flag,k =  self.solution(alpha,k,flag,lst,ra,de,v)
        return lst,flag,k 


# In[ ]:


@ray.remote
def mainloop(file,H0,omegamc,omegalc,omegakc,c,dcondc,vcondc,nmin):
    print("start")
    ti = time.time()

    field = np.loadtxt(file)
    field = field[field[:,2].argsort()]
    ##########################
    #                        #
    #                        #
    #    common paramters    #
    #                        #
    #                        #
    ##########################

#     fname = ["N"] 
#     fra = [-99.]
#     fde = [-99.]
#     fz = [-99]
#     fnum = [-9.] 
    ra = field[:,0]
    dec = field[:,1]
    z = field[:,2]

    ID = field[:,3].astype("str")
    v=z*c
    
    ngal = len(ra)
    cosmo = FlatLambdaCDM(H0 = H0, Om0 = omegamc)
    sdcondc =  cosmo.arcsec_per_kpc_proper(z)*dcondc*u.kpc/u.arcsec
    gname = np.ones(ngal)*(-1)    
    ngroup = 0 
    flag = np.zeros(ngal)
    for i in range(ngal):
        """
        Root Node(s)
        """
        
        lst = np.array([-1 for _ in range(ngal)])
        if (flag[i] != 0): continue  
        k = 0 
        lst[k] = i 
        flag[i] = 1 
        fof = fofradecV(H0,omegamc,omegalc,omegakc,c,sdcondc,vcondc)
        lst,flag,k = fof.solution(i,k,flag,lst,ra,dec,v)

        if (k >= nmin-1):
            l0 = lst[0]
            ind = np.where(lst >= 0)[0].astype(int)
            cnt = ind.size
            str1 = ID[l0]

            str1 = str1.replace(" ","")
            gname[lst[ind]] = str1
#             fname.append(str1) 

#             toto1 = np.where(ra[lst[ind]] < 90)[0]
#             ntoto1 = toto1.size

#             toto2 = np.where(ra[lst[ind]] > 270)[0]
#             ntoto2 = toto2.size 

    
            ngroup += 1 
    tf = time.time()

#     if ngroup >= 1:
#         fname = fname[1:ngroup+1] 
#         fra = fra[1:ngroup+1]
#         fde = fde[1:ngroup+1]
#         fz = fz[1:ngroup+1]
#         fnum = fnum[1:ngroup+1]
    
    # Time check Min/Sec
    print(f'{(tf-ti)//60} mins {((tf-ti)%60)//1} second')                

    idx = np.where(gname != -1)[0]
    arr = np.array([ID[idx],ra[idx],dec[idx],z[idx],gname[idx]]).astype(float).T

    return arr

