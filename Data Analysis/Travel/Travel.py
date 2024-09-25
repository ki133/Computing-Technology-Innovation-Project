# travel_dataset_visualization.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the travel dataset
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Travel Data/travel_dataset.xlsx"
travel_data = pd.read_excel(file_path)

# Check the column names
print("Columns in the dataset:", travel_data.columns)

# Drop rows with missing data
travel_data.dropna(inplace=True)

# 1. **Total Revenue Passengers Over Time by City Pair Route**
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Total rev pax (U/D)', data=travel_data, marker='o')
plt.title('Total Revenue Passengers (U/D) Over Time')
plt.xlabel('Year')
plt.ylabel('Total Revenue Passengers (U/D)')
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.show()

# Explanation:
# This chart shows the trend of total revenue passengers over time (in "U/D" format, which might mean "Up/Down" or a related metric). 
# You can use this chart to observe how the number of passengers changes each year, which could reveal important trends, such as growth or declines in passenger numbers.

# 2. **Seats vs. RPKs Scatter Plot**: Correlation between available seats and Revenue Passenger Kilometers (RPKs)
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Available seats', y='Total RPK', data=travel_data)
plt.title('Available Seats vs. Revenue Passenger Kilometers (RPKs)')
plt.xlabel('Available Seats')
plt.ylabel('Total RPK')
plt.grid(True)
plt.tight_layout()
plt.show()

# Explanation:
# This scatter plot compares the number of available seats with total revenue passenger kilometers (RPKs).
# A strong positive correlation would indicate that as more seats become available, more passenger kilometers are being generated, suggesting a higher demand or usage of flight capacity.

# 3. **Correlation Heatmap**: Correlation between various numerical columns
plt.figure(figsize=(10, 8))
corr_matrix = travel_data[['Total rev pax (U/D)', 'Total rev pax (TOB)', 'Total RPK', 'Available seats']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap (Travel Dataset)')
plt.tight_layout()
plt.show()

# Explanation:
# This heatmap visualizes the correlation between key numerical variables, including revenue passengers, RPKs, and available seats.
# Correlation values range from -1 to 1, where 1 means a perfect positive correlation, -1 means a perfect negative correlation, and 0 means no correlation. 
# Use this chart to understand which variables are most closely related to each other, which might indicate stronger relationships between certain flight metrics.