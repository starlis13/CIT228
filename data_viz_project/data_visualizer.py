import csv
import matplotlib.pyplot as plt
import numpy as np
import datetime

def GetDataSetFromCSV(filename):
    dataPoints=[]
    months=[]
    buckets=[]

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        header_row=next(csv_reader)
        
        for row in csv_reader:        
            if not buckets.__contains__(row):
                buckets.append(row)
                
                if row[0]=='NULL':
                    months.append(0)
                else:
                    months.append(float(row[0]))
                
                if row[1]=='NULL':
                    dataPoints.append(0)
                else:
                    dataPoints.append(float(row[1]))
                    
    return [dataPoints, months, buckets]

def displaySalesforceBudget():
    dataSet = GetDataSetFromCSV('salesforce_budget.csv')

    fig = plt.figure()
    ax1 = fig.add_subplot()  

    ax1.scatter(dataSet[0], dataSet[0], c=dataSet[0], cmap=plt.cm.Reds, label="Total Monthly SF Budget")

    ax1.set_ylabel("US Dollars")
    ax1.set_xlabel("Month")
    ax1.set_xticklabels(dataSet[1])
    ax1.set_title("Total Monthly Financial Investment")

    plt.suptitle("Salesforce Analysis")
    plt.show() 

def displaySalesforceLicenses():
    dataSet = GetDataSetFromCSV('salesforce_licenses.csv')
    
    plt.barh(dataSet[1], dataSet[0], color ='darkgreen', height = 0.75) 
    
    plt.xlabel("Month") 
    plt.ylabel("Licenses") 
    plt.title("Salesforce License Growth") 
    plt.show() 

def displaySalesforceTechDebt():
    dataSet = GetDataSetFromCSV('salesforce_tech_debt.csv')

    fig = plt.figure()
    ax1 = fig.add_subplot()  

    ax1.plot(dataSet[1], dataSet[0], c="#acacac", marker="o")

    plt.suptitle("Salesforce Tech Debt")
    plt.show()

def displayCustomSystemBudget():
    dataSet = GetDataSetFromCSV('custom_system_budget.csv')

    fig = plt.figure()
    ax1 = fig.add_subplot()  

    ax1.scatter(dataSet[0], dataSet[0], c=dataSet[0], cmap=plt.cm.Greens, label="Total Monthly Custom System Budget")

    ax1.set_ylabel("US Dollars")
    ax1.set_xlabel("Month")
    ax1.set_xticklabels(dataSet[1])
    ax1.set_title("Total Monthly Financial Investment")

    plt.suptitle("Custom System Analysis")
    plt.show() 

def displayCustomSystemLicenses():
    dataSet = GetDataSetFromCSV('custom_system_licenses.csv')

    plt.plot(dataSet[1], dataSet[0], c="#acacac", marker="o") 
    
    plt.xlabel("Month") 
    plt.ylabel("Staff Members") 
    plt.title("Custom System Staff Need") 
    plt.show() 

def displayCustomSystemTechDebt():
    dataSet = GetDataSetFromCSV('custom_system_tech_debt.csv')

    fig = plt.figure()
    ax1 = fig.add_subplot()  

    ax1.plot(dataSet[1], dataSet[0], c="cyan", marker="o")

    plt.suptitle("Custom System Tech Debt")
    plt.show()

def displayComparativeBudgets():
    customSystemDataSet = GetDataSetFromCSV('custom_system_budget.csv')
    salesforceSystemDataSet = GetDataSetFromCSV('salesforce_budget.csv')

    barWidth = 0.25

    br1 = np.arange(len([customSystemDataSet[0]])) 
    br2 = [x + barWidth for x in br1]

    plt.bar(br1, customSystemDataSet[0], color ='cyan', width=barWidth, label="Custom System")
    plt.xticks([customSystemDataSet[0][-1], salesforceSystemDataSet[0][-1]])
    
    plt.bar(br2, salesforceSystemDataSet[0], color="purple",  width=barWidth, label="Salesforce")
    
    
    plt.ylabel("Dollars (USD in Millions)") 
    plt.xlabel("Systems")
    plt.title("Comparative Budgets")
    plt.legend(loc="best")
    plt.show() 

# Display Salesforce Charts

#displaySalesforceTechDebt()
#displaySalesforceLicenses()
#displaySalesforceBudget()

#displayCustomSystemTechDebt()
#displayCustomSystemLicenses()
#displayCustomSystemBudget()

displayComparativeBudgets()