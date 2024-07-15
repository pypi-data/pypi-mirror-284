### Welcome to using Parallelizing Friends Of Friends. 

I'm an undergraduate at the Exo-galaxy Lab in Chungnam National University. 
If you have any questions or feedback about PFOF code, Place contact us at the email address below.
I want your opinions and thoughts about the code. Please feel free to contact me! 
<Email : 98ehddbs@naver.com>

-------------------------------------------------------------------------------------------------
## Required Packages 
                           
* necessary library 
* Numpy
* Pydl                            
* Ray (Multiprocessing Package)
* astropy
* Pandas 
* tqdm (processing bar)
* time (Total time check)
* sys (set recursionlimit) 

Version 1.0.4 2023.06.27
Version of packages used. (Please check these versions)

**python  3.9.18
numpy   1.24.0
astropy 5.1.1
pandas  2.1.4
pydl    0.7.0 
**ray     2.2.0 -> very sensitive to version

You must check the versions of these libraries ! If CNUFOF doesn't run, you need to change some version.

*** Based on observing data Parallelizing Friends of Friends algorithm *** 
ra (0~360[degree]), dec (-90~90[degree]), redshift (>=10^(-3))


Note) 
- Set linking length [Physical Distance [kpc] | velocity [km/s]] , nmin(minimum number of particles(galaxies)) 

- The group name you run as whole at once may be different from the group you run in parallel. But, The particles found for each group will be the same 

- When setting the variables, you should follow the example.

More detail usage methods are explained in "example" and "Explanations file for each code"  file 

Thank you. 