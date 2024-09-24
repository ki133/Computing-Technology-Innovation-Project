import pandas as pd
import numpy as np

# Path to your file
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Data/monthly-airline-performance-june-2024.xlsx"

# Load the second sheet and skip unnecessary header rows (adjust skiprows as needed)
domestic_airline_data = pd.read_excel(file_path, sheet_name='Domestic airlines', skiprows=3)

# Rename the columns
domestic_airline_data.columns = ['Year', 'Month', 'Hours flown', 'Aircraft km flown', 'Aircraft departures', 
                                 'Total rev pax (U/D)', 'Freight tonnes (U/D)', 'Mail tonnes (U/D)', 
                                 'Total rev pax (TOB)', 'Freight tonnes (TOB)', 'Mail tonnes (TOB)', 
                                 'Total RPK', 'Pax tonne km', 'Freight tonne km', 'Mail tonne km', 
                                 'Total tonne km', 'Available seat km', 'Available tonne km', 'Available seats', 
                                 'Pax load factor %', 'Weight load factor %', 'Total pax', 'Charter pax', 'Charter aircraft departures']

# Replace '*' values with NaN (Not a Number)
domestic_airline_data.replace('*', np.nan, inplace=True)

# Convert the 'Year' column to numeric, forcing errors (non-numeric values) to NaN
domestic_airline_data['Year'] = pd.to_numeric(domestic_airline_data['Year'], errors='coerce')

# Filter data to only include years from 2010 onwards
domestic_airline_data_filtered = domestic_airline_data[domestic_airline_data['Year'] >= 2010]

# Round all numeric columns to 2 decimal places
domestic_airline_data_filtered = domestic_airline_data_filtered.round(2)

# Sort the data by Year and Month
domestic_airline_data_sorted = domestic_airline_data_filtered.sort_values(by=['Year', 'Month'], ascending=[True, True])

# Display the sorted data
print(domestic_airline_data_sorted.head())

# Save the sorted and cleaned data to a new file
output_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Data/travel_dataset.xlsx"
domestic_airline_data_sorted.to_excel(output_path, index=False)

print("Data from 2010 onwards, rounded, sorted, and saved to travel_dataset.xlsx")