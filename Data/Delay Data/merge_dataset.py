import pandas as pd

# Path to the Excel file with multiple sheets
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Delay Data/delay_dataset.xlsx"  # Ensure the file is a .xlsx file

# Load the Excel file
excel_file = pd.ExcelFile(file_path)

# Create an empty list to store each sheet's data
all_sheets = []

# Loop through all the sheets and append each to the list
for sheet_name in excel_file.sheet_names:
    df = pd.read_excel(excel_file, sheet_name=sheet_name, engine='openpyxl')  # Specifying 'openpyxl' engine for Excel files
    all_sheets.append(df)

# Concatenate all the sheets into a single DataFrame
merged_data = pd.concat(all_sheets, ignore_index=True)

# Save the merged data to Done_dataset.csv in the same path
output_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Delay Data/Done_delay_dataset.csv"
merged_data.to_csv(output_path, index=False)  # Save as CSV in the same path

print("All sheets merged and saved to Done_dataset.csv successfully!")