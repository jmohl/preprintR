# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 20:12:02 2020

@author: Jeff
"""

#This data was taken from https://www.economist.com/graphic-detail/2020/05/30/how-to-spot-dodgy-academic-journals using webplotdigitizer
#remaking the plot 

import matplotlib.pyplot as plt
import pandas as pd

def make_plot(data_path ='D:\GitHub\preprintR\data\raw\dodgy_journals.csv'):
    df= pd.read_csv(data_path)
    
    #need to add dates and strip data (most recent is 2018, want to go back to 2000)
    years = list(reversed(range(2020-len(df),2020)))
    df['pred'] = years
    df.rename(columns = {'pred':'year', 'Unnamed: 1': 'Predatory','Unnamed: 3': 'Reliable'},inplace = True)
    df = df[['year','Predatory','Reliable']]
    df = df.drop(0) #dropping header row
    df[['Predatory','Reliable']]=df[['Predatory','Reliable']].astype(float).round(2)
    #note that predatory counts and reliable counts are reversed from one another
    df['Predatory'] = df['Predatory'].values[::-1]
    df['Predatory'] = df['Predatory']-df['Reliable'] #extracted data was already the result of a sum, reversing that here
    
    df = df[::-1]
    #done with data cleaning, note the counts are in 1000s
    df.plot.bar(x='year', y=['Reliable','Predatory'], stacked = True)
    plt.ylabel('Cumulative Journal Count - 1000s')
    plt.xlabel('year')
    plt.title('A large number of dubious journals have launched in the last decade')
    plt.show()
    return
