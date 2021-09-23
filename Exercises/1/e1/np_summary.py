import numpy as np
import math as m

data = np.load('/Users/jonathanperalgort/Documents/CMPT353-Computational-Data-Science/Exercises/1/e1/monthdata.npz') #loading the monthdata.npz file

totals = data['totals']

counts = data['counts']

sum_of_precipitations_per_location = np.sum(totals, axis=1)

sum_of_precipitations_per_location #sum of monthly precipitations per location

np.argmin(sum_of_precipitations_per_location) #Displays the location with the least precipitation throughout the year

totals/counts

sum_of_monthly_precipitations = np.sum(totals, axis=1) #sum of total monthly precipitations

sum_of_monthly_precipitations

sum_of_counts = np.sum(counts, axis=1) #sum of counts
sum_of_counts

sum_of_monthly_precipitations / sum_of_counts #Divided by twelve to figure out the average precipitation in a city per year

#new_totals will contain the reshaped totals array with the precipitations of the corresponding quarter
new_totals = totals

new_totals = np.reshape(new_totals, (9,4,3))

sum_of_quarters = np.sum(new_totals, axis=2) #contains the sum of all the quarters in the year for all 9 locations

sum_of_quarters/3 #displays the average of precipitations per quarter for each of the 9 locations