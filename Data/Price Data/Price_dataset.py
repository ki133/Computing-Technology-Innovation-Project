import pandas as pd

# Correct file path to the location on your local machine
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Done_price_dataset.csv"

# Load the CSV file
price_df = pd.read_csv(file_path)

# 1. Drop the unnecessary 'Unnamed: 8' column
if 'Unnamed: 8' in price_df.columns:
    price_df = price_df.drop(columns=['Unnamed: 8'])

# 2. Check for duplicates and remove them
price_df.drop_duplicates(inplace=True)

# 3. Standardize city and route names (strip whitespace and ensure proper capitalization)
price_df['Port1'] = price_df['Port1'].str.strip().str.title()
price_df['Port2'] = price_df['Port2'].str.strip().str.title()
price_df['Route'] = price_df['Route'].str.strip().str.title()

# 4. Round the numeric columns ($Value and $Real) to 2 decimal places
price_df['$Value'] = price_df['$Value'].round(2)
price_df['$Real'] = price_df['$Real'].round(2)

# 5. Summary statistics for $Value and $Real columns (after rounding)
price_summary = price_df[['$Value', '$Real']].describe()

# Save the cleaned file
output_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Cleaned_Done_price_dataset.csv"
price_df.to_csv(output_path, index=False)

# Display the summary statistics
print(price_summary)