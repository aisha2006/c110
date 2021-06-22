import pandas as pd
import csv
import plotly.figure_factory as ff
import statistics as st
import random 

df = pd.read_csv("newdata.csv")
temp = df["average"].tolist()
fig = ff.create_distplot(
    [temp],["Temperature"],show_hist = False
)
# fig.show()  
# mean = st.mean(temp)
# stdev = st.stdev(temp)
# print(mean,stdev)

#Mean and stdev of any random data points

def random_set_of_mean(counter):
    sample = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(temp)-1)
        value = temp[randomIndex]
        sample.append(value)

    mean = st.mean(sample)
    #stdev = st.stdev(sample)
    return mean

#To plot the mean on the graph
def show_figure(meanlist):
    df = meanlist
    fig = ff.create_distplot(
        [df],["meanlist"],show_hist = False
    )
    fig.show()
    mean = st.mean(meanlist)
    print(mean)

#Mean of random 100 data points taken 1000 times
def setup():
    meanlist = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        meanlist.append(set_of_means)
    show_figure(meanlist)

setup()

def stdev():
    meanlist = []
    for i in range(0,1000):
        set_of_means = random_set_of_mean(100)
        meanlist.append(set_of_means)
    stdev = st.stdev(meanlist)
    print(stdev)

stdev()