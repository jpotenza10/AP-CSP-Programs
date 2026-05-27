#Jordan Potenza
#Init
import pandas as pd
data=pd.read_csv('hacker.csv')
log_ID = data['Log_ID'].tolist()
address = data['IP_Address'].tolist()
protocol = data['Protocol'].tolist()
data_KB = data['Data_KB'].tolist()
time = data['Time'].tolist()
description= data['Description'].tolist()

filter=[]
#Function
def failed(word):
    for i in range(len(log_ID)):
        if (word) in description[i]:
            filter.append([i])
    print(filter)
    filter.clear()
    print(data.loc[196])

def find(amount):
    for i in range(len(data_KB)):
        if data_KB[i]>amount:
            filter.append([i])
    print(filter)
    filter.clear()
    print(data.loc[199])

def force(reset):
        for i in range(len(description)):
            if(reset)in description[i]:
                filter.append([i])

        print(len(filter))
        filter.clear()
force("Force")
print(data.loc[[204,205,207,210,214,218,221,222,224,231,235]])

#Main
force('Forced')
