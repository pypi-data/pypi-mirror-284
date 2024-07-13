# pyrustats package
A simple package about statistics made by Ruukha  <br />
Currently it can only do Gaussian and Binomial distributions  <br />

# Files
Generaldistribution.py creates the 'Distribution' class for the distribution types to inherit  <br />
Gaussiandistribution.py creates the 'Gaussian' class  <br />
Binomialdistribution.py creates the 'Binomial' class  <br />
Both Gaussian and Binomial class files create functions to calculate the mean, standard deviation, probability density function (pdf), histogram, and a function to plot the normalized histogram of the data and a plot of the pdf along the same range  <br />

# Installation
No special requirements other than matplotlib  <br />

# Changelog
0.2.1: cleaned the code, fixed the package importing with a wrong name.  <br /> 
In Binomialdistribution, if you add a file path as an argument to replace_stats_with_data, it will automatically call read_data_file. Else it will work as previously  
<br />

# License