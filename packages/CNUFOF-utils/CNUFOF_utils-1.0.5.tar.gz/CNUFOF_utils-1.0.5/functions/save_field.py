#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import astropy.cosmology 
import astropy.units as u
import pandas as pd
from astropy.cosmology import FlatLambdaCDM , Planck18


# In[ ]:


#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np 
import astropy.cosmology 
import astropy.units as u
import pandas as pd
from astropy.cosmology import FlatLambdaCDM , Planck18


# In[ ]:

class nc_all_sky_divide():
    def __init__(self,file,div_ra,div_dec,H,omegamc,dcondc):
        self.ra = np.array(file.ra)
        self.dec = np.array(file.dec)
        self.z = np.array(file.redshift)
        self.h0c = H 
        self.omegamc = omegamc 
        self.dcondc = dcondc 
        self.div_ra = div_ra
        self.div_dec = div_dec
        self.min_z = min(file.redshift)
        
    def no_com_dec(self):
        dec = self.dec
        z = self.z
        min_z = self.min_z
        div_dec = self.div_dec
        dec_index_parallel_field = []

        alpha = abs(int(max(dec)+1)-int(min(dec)-1))/div_dec
        
            
        cosmo = FlatLambdaCDM(H0 = self.h0c, Om0 = self.omegamc)
        link_len = cosmo.arcsec_per_kpc_proper(min_z)/3600.*self.dcondc*u.kpc/u.arcsec #[degree]
        print("linkling_angular is",link_len,"[degree]")
        beta = min(dec)+((alpha-link_len)*div_dec)

        gamma = (max(dec)-beta)/(alpha-link_len)
        if (gamma == int(gamma)):
            gamma = gamma
        else:
            gamma += 1 
        
        div_dec += int(gamma)
        print("total divided field :", int(div_dec))
        f_dec = int(min(dec)-1)
        dec_index_parallel_field = []
        for _ in range(div_dec):
        
            if f_dec != int(min(dec)-1):
                if (f_dec) >=0: 
                    idx = np.where((dec>=(f_dec-link_len))&(dec<=f_dec+alpha))[0].astype(int)
                    f_dec += alpha-link_len
                else:
                    if (f_dec+alpha) >=0:
                        idx = np.where((dec>=f_dec-link_len)&(dec<=f_dec+alpha))[0].astype(int)
                        f_dec += alpha-link_len
                    
                    else:
                        idx = np.where((dec>=f_dec-link_len)&(dec<=f_dec+alpha))[0].astype(int)
                        f_dec += alpha-link_len
                        
            else: 
                idx = np.where(dec<=min(dec)+alpha)[0].astype(int)
                f_dec+= alpha-link_len
            dec_index_parallel_field.append(idx)
        return dec_index_parallel_field
    
    
def save_file(file,div_ra,div_dec,H,omegamc,dcondc,dir2):
    lst = nc_all_sky_divide(file,div_ra,div_dec,H,omegamc,dcondc).no_com_dec()
    for i in range(len(lst)): 
        imfo = np.array([np.array(file.ra)[lst[i]],np.array(file.dec)[lst[i]],np.array(file.redshift)[lst[i]],np.array(file.ID)[lst[i]]]).T
        np.savetxt(dir2+"field_"+str(i),imfo)

    

