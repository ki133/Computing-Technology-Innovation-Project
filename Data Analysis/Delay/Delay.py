import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Load the delay dataset from the updated Excel file
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Delay Data/Updated_Delay_Dataset.xlsx"
delay_data = pd.read_excel(file_path)

# Drop rows with missing data (if necessary)
delay_data.dropna(inplace=True)

# Ensure 'Year' and 'Month' columns are combined to a datetime object for plotting over time
delay_data['YearMonth'] = pd.to_datetime(delay_data['Year'].astype(str) + delay_data['Month'].astype(str), format='%Y%m', errors='coerce')

# Drop rows where 'YearMonth' couldn't be parsed (if necessary)
delay_data = delay_data.dropna(subset=['YearMonth'])

# 1. **Plot: Delay Rate Over Time with Average Line**
delay_data['Delay Rate (%)'] = (delay_data['Departures Delayed'] / delay_data['Sectors Flown']) * 100
average_delay_rate = delay_data['Delay Rate (%)'].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x='YearMonth', y='Delay Rate (%)', data=delay_data, marker='o', label='Delay Rate')
plt.axhline(average_delay_rate, color='red', linestyle='--', label='Average Delay Rate')
plt.title('Delay Rate Over Time (With Average Line)')
plt.xlabel('Year-Month')
plt.ylabel('Delay Rate (%)')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()

# **Explanation**: 
# This chart visualizes the percentage of delayed departures over time. The delay rate is calculated as the number of delayed departures divided by the number of sectors flown. 
# The red dashed line represents the average delay rate across the entire dataset, making it easier to compare the monthly performance with the overall trend.

# 2. **Plot: Cancellation Rate Over Time with Average Line**
delay_data['Cancellation Rate (%)'] = (delay_data['Cancellations'] / delay_data['Sectors Scheduled']) * 100
average_cancellation_rate = delay_data['Cancellation Rate (%)'].mean()

plt.figure(figsize=(10, 6))
sns.lineplot(x='YearMonth', y='Cancellation Rate (%)', data=delay_data, marker='o', label='Cancellation Rate')
plt.axhline(average_cancellation_rate, color='green', linestyle='--', label='Average Cancellation Rate')
plt.title('Cancellation Rate Over Time (With Average Line)')
plt.xlabel('Year-Month')
plt.ylabel('Cancellation Rate (%)')
plt.xticks(rotation=45)
plt.legend(loc='upper right')
plt.grid(True)
plt.tight_layout()
plt.show()

# **Explanation**: 
# This chart shows the cancellation rate over time, calculated as the number of canceled flights divided by the number of scheduled sectors. 
# The green dashed line represents the average cancellation rate, which allows for easy comparison of specific months to the overall cancellation trend.

# 3. **Plot: Log-Transformed Distribution of Delayed Departures**
plt.figure(figsize=(10, 6))
sns.histplot(np.log1p(delay_data['Departures Delayed']), bins=30, kde=False, color='blue')
plt.title('Log-Transformed Distribution of Delayed Departures')
plt.xlabel('Log(Number of Delayed Departures)')
plt.ylabel('Count')
plt.grid(True)
plt.tight_layout()
plt.show()

# **Explanation**: 
# This histogram displays the distribution of delayed departures using a log-transformation to better visualize the distribution of the data. 
# The log transformation reduces the impact of extreme values, making the distribution easier to analyze, particularly when the data includes a wide range of values.

# 4. **Plot: Log-Transformed Distribution of Cancellations**
plt.figure(figsize=(10, 6))
sns.histplot(np.log1p(delay_data['Cancellations']), bins=30, kde=False, color='red')
plt.title('Log-Transformed Distribution of Cancellations')
plt.xlabel('Log(Number of Cancellations)')
plt.ylabel('Count')
plt.grid(True)
plt.tight_layout()
plt.show()

# **Explanation**: 
# Similar to the previous plot, this chart shows the distribution of flight cancellations, log-transformed to manage any skewness in the data. 
# The transformation helps present the cancellation data in a way that allows for easier comparison of frequencies across different ranges.

# 5. **Plot: Correlation Matrix Heatmap (for understanding the relationship between numeric features)**
plt.figure(figsize=(10, 8))
corr_matrix = delay_data[['Departures Delayed', 'Sectors Flown', 'Cancellations', 'Sectors Scheduled']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix Heatmap (Delay Dataset)')
plt.tight_layout()
plt.show()

# **Explanation**: 
# This heatmap displays the correlation between key numerical features in the dataset, such as the number of delayed departures, cancellations, and sectors flown. 
# The correlation values range from -1 to 1, where values close to 1 indicate a strong positive correlation, and values close to -1 indicate a strong negative correlation. 
# This plot helps to identify the relationships between different flight metrics, potentially revealing patterns in the data.