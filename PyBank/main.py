import os 
import csv
import pandas as pd

budget_csv = os.path.join('Resources','budget_data.csv')

results = pd.read_csv('budget_data.csv')
print("Total Months: ", len(results))
