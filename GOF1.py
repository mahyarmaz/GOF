all_lines = []
freqs = []
nrml_freqs=[]

with open ('Goutput_Freq4.txt', 'r') as file:                      #opens a Gaussian Frequency text file
    for each_line in file:
        all_lines.append(each_line.strip())
        if "Frequencies --" in each_line:
            freqs.append(each_line.split())

for i in range(len(freqs)):
    nrml_freqs.append(list(map(float, freqs[i][2:5])))             #reads normal vibrational frequencies

n=0
for a in range(len(nrml_freqs)):                                    #counting imaginary numbers
    for b in range(3):
        if nrml_freqs[a][b] < 0:
            n=n+1
print(f"there are {n} imaginary frequencies", '\n')

import numpy as np
import math
from scipy import constants

h = constants.Planck
kb = constants.Boltzmann
r = constants.gas_constant
temp=298.15

nrml_freqs=np.array(nrml_freqs)                                          #make arrays of frequencies
wavenumber = nrml_freqs * constants.c *100                               #convert to wavenumber
gamma = (h*wavenumber)/(kb*temp)                                         #calculating gamma

each_entropy = []
for a in range(len(gamma)):                                               #calculating each entropy
    for b in range(3):
        if gamma[a][b] > 0:
            each_entropy.append(r*(((gamma[a][b]) / (math.exp(gamma[a][b]) - 1)) - math.log(1 - math.exp(-gamma[a][b]))))

sigma = 0
for e in range(len(each_entropy)):                                           # calculating total entropy
   sigma = sigma + each_entropy[e]

print(f'The total vibrational entropy is: {sigma} J/mol.K or {(sigma / 4.184)} Cal/mol.K')