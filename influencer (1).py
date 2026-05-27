#Jordan Potenza
#Init
import pandas as pd
data=pd.read_csv('influencer.csv')
#Functions
month = data['Month'].tolist()
views = data['Views'].tolist()
dislikes = data['Dislikes'].tolist()
subs = data['Subscriber(+-)'].tolist()
revenue = data['Revenue'].tolist()
filter = []

def humble(high):
    for i in range(len(month)):
        if views[i] < high:
            filter.append([i])
    print(filter)
    filter.clear()


def golden(high):
    for i in range(len(month)):
        if subs[i]>high:
            filter.append([i])
    print(filter)
    filter.clear()


def scandal(cash):
    for i in range(len(month)):
        if revenue[i]==cash:
            filter.append([i])
    print(filter)
    filter.clear()

#Main
humble(2000)
golden(50000)
scandal(0)
