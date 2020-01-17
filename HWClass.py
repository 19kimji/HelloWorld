# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 13:18:14 2016

@author: James D. Berger

Hardy Weinberg Simulation
This progam allows one to examine the effects of 
selection on gene frequencies over the course of 
generations.

Inputs:
A -- Initial allele frequency in population
a -- Initial allele frequency in population
FAA -- fitness of AA phenotype
FAa -- fitness of Aa phenotype
Faa -- fittness of aa phenotype
gen -- number of generations to run
"""
# Define functions

def getGenotypeFreqs(A1,A2): # Returns genotype frequencies for
    global A1A1,A1A2,A2A2# next generation assumes reandom mating
    A1A1=A1*A1#Write your function here
    A1A2=2*A1*A2
    A2A2=A2*A2#print ('in function: A1A1,A1A2,A2A2',A1A1,A1A2,A2A2)
    

def getAlleleFreqs(A1A1,A1A2,A2A2): #Returns allele freqs. for next gen.
    global A1,A2
    NA1=2*A1A1*FA1A1 + A1A2*FA1A2
    NA2=2*A2A2*FA2A2 + A1A2*FA1A2
    A1=NA1/(NA1+NA2)
    A2=1.0-A1 #Write your function here
    

def StoreData(): #Appends current data to the storage arrays
    g.append(i) # Store present values
    fA2.append(A2)
    fA1.append(A1)
    Ahom.append(A1A1) #Append data to be plotted
    ahom.append(A2A2)
    Ahet.append(A1A2)
  
def PlotFigures(): #Plots genotype and allele frequencies vs. gen
        
    plt.figure(1)
    plt.axis([0.0,gen,0.0,1.0])
    plt.plot(g,Ahom,'r-',label='A1A1') #plot()
    plt.plot(g,Ahet,'k-',label='A1A2')
    plt.plot(g,ahom,'g-',label='A2a2')
    plt.legend(loc=5)
    plt.xlabel('Generation')
    plt.ylabel('Genotype Frequency')
    plt.show()
    plt.figure(2)
    plt.axis([0.0,gen,0.0,1.0])
    plt.plot(g,fA2,'g-',label='A2')
    plt.plot(g,fA1,'r-',label='A1')
    plt.plot([0,gen],[0.02,0.02],'k-',label='2%') #plot 2% line
    plt.legend(loc=5)
    plt.xlabel('Generation')
    plt.ylabel('Allele Frequency')
    plt.show()
    print ('Fittness: A1A1',FA1A1,'A1A2',FA1A2,'A2A2',FA2A2)
    print ('initial allele frequencies: A1=',fA1[0],'A2=',fA2[0])
    print('Number of generations run', i)
    print ('final genotype frequencies: \nA1A1=',A1A1,'\nA1A2=',A1A2,
           '\nA2A2=',A2A2)
    print ('final allele frequencies: \nA1=',A1,'\nA2=',A2)
# Main progam begins here                
import matplotlib.pyplot as plt
#Set parameters

#Start by entering initial allele freguencies
A1=0.001 #A allele frequency. 
A2=1.0-A1 #a allele frequency
#Then enter fitnesses of each genotype
FA1A1=1.0 #Fitness of A1A1 phenotype Enter fitness of phenotypes here
FA1A2=1.0 #Fitness of A1A2 phenotype
FA2A2=0.7 #Fitness of A2A2 phenotype
#Enter number of generations for simulation to run
gen=200 #Number of generations to run
#vectors for storing data to be graphed
Ahom=[] #A1A1 homozygote freq for each generation
ahom=[] #A2A2 homozygote freq for each gen.
Ahet=[] #A1A2 heterozygote freq for each gen.
g=[] # number of the present generation
fA2=[] #frequency of A2
fA1=[] #frequency of A1
#-------------------
#Calculate initial genotype frequencies
# Get genotype frequencies for gen 0

getGenotypeFreqs(A1,A2)
i=0 #generation counter
while (i<gen and A2>0.02): #A2>0.02 i<gen:
    StoreData() #Store present values 
    i+=1 # Increment counter
    getAlleleFreqs(A1A1,A1A2,A2A2)#Calculate allele freqs. for this gen. 
    getGenotypeFreqs(A1,A2) #Calculate genotype freqs. for this gen. 

PlotFigures()