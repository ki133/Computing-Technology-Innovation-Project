import pandas as pd
import numpy as np

# Provide your actual file path on your local machine
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Done_delay_dataset.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, low_memory=False)

# Replace 'na' and other invalid values with NaN
df.replace('na', np.nan, inplace=True)

# Sort the data by 'Month'
df_sorted = df.sort_values(by='Month', ascending=True)

# Convert numeric columns and handle errors (coercing non-numeric values to NaN)
numeric_columns = ['OnTime Departures \n(%)', 'OnTime Arrivals \n(%)', 'Cancellations \n\n(%)']
df_sorted[numeric_columns] = df_sorted[numeric_columns].apply(pd.to_numeric, errors='coerce').round(2)

# Save the sorted and rounded data back to a new CSV file
output_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Updated_Done_delay_dataset.csv"
df_sorted.to_csv(output_path, index=False)

print("Updated and saved as Updated_Done_delay_dataset.csv")
