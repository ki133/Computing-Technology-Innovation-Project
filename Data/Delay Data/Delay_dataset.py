import pandas as pd

# Load the CSV file and handle mixed data types
file_path = 'C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Delay Data/Done_delay_dataset.csv'

# Using low_memory=False to avoid the DtypeWarning and let pandas handle data chunks
delay_data = pd.read_csv(file_path, low_memory=False)

# Separate 'Year' and 'Month' from the 'Month' column (assuming 'Month' is formatted like 'YYYY-MM')
delay_data['Year'] = pd.to_datetime(delay_data['Month'], errors='coerce').dt.year
delay_data['Month'] = pd.to_datetime(delay_data['Month'], errors='coerce').dt.month

# Drop rows where Year or Month could not be parsed
delay_data.dropna(subset=['Year', 'Month'], inplace=True)

# Sort the data by 'Year' and 'Month'
delay_data = delay_data.sort_values(by=['Year', 'Month'], ascending=[True, True])

# Extract rows where 'Route' equals 'All Ports - All Ports' and save them to a new file
all_ports_data = delay_data[delay_data['Route'] == 'All Ports-All Ports']

# Save the 'All Ports - All Ports' data to a new Excel file
all_ports_file_path = 'C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Delay Data/All_Ports_Delay.xlsx'
all_ports_data.to_excel(all_ports_file_path, index=False)

# Remove rows with 'All Ports - All Ports' and 'All Airlines' from the original dataset
filtered_delay_data = delay_data[(delay_data['Route'] != 'All Ports-All Ports') & (delay_data['Airline'] != 'All Airlines')]

# Output file path for the updated Excel file without 'All Ports - All Ports' and 'All Airlines'
updated_file_path = 'C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Delay Data/Updated_Delay_Dataset_Without_All_Ports_All_Airlines.xlsx'

# Save the filtered data as an Excel file
filtered_delay_data.to_excel(updated_file_path, index=False)

print(f"'All Ports - All Ports' data saved to {all_ports_file_path}")
print(f"Filtered data (without 'All Ports - All Ports' and 'All Airlines') saved to {updated_file_path}")