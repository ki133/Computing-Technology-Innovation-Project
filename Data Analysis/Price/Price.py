import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import numpy as np

# Load the dataset
file_path = "C:/Users/anhki/OneDrive/Documents/Swinburne/Year_2_Sem_1/Innovation Project/Assingment 2/Data/Price Data/Cleaned_Done_price_dataset.csv"
data = pd.read_csv(file_path)

# Fixing the 'YearMonth' issue
# Convert YearMonth to strings and then extract Year and Month
data['YearMonth'] = data['YearMonth'].astype(str)
data['Year'] = data['YearMonth'].str[:4]  # Extract first 4 characters as Year
data['Month'] = data['YearMonth'].str[4:]  # Extract last 2 characters as Month

# Convert Year and Month to integers
data['Year'] = pd.to_numeric(data['Year'], errors='coerce')
data['Month'] = pd.to_numeric(data['Month'], errors='coerce')

# Drop rows with invalid Year/Month (if any)
data = data.dropna(subset=['Year', 'Month'])

# Streamlit App Title
st.title('Flight Price Data Analysis')

# Display the cleaned data
if st.checkbox('Show cleaned data'):
    st.write(data)

# --- Chart 1: Median Price Trends Over Time (Overall) ---
# Aggregating data to show the median price for each year
yearly_median_prices = data.groupby('Year')['$Value'].median().reset_index()

# Plot using Matplotlib
st.subheader('Flight Price Trends Over Time (Median Yearly Prices)')
fig1, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(yearly_median_prices['Year'], yearly_median_prices['$Value'], marker='o', linestyle='-', label='Median Flight Prices')
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Median Price ($)', fontsize=12)
plt.xticks(rotation=90)
plt.title('Median Flight Prices Over Time (Yearly)')
st.pyplot(fig1)

# Explanation:
st.write("**Explanation**: This chart shows the overall trend of median flight prices over time. It helps us understand whether flight prices have been increasing or decreasing over the years. This can reveal potential seasonal changes or overall trends in the market.")

# --- Chart 2: Price Trends by Route (With Scroll Box) ---
# Adding a filter to visualize price trends by route
routes = data['Route'].unique()
selected_route = st.selectbox('Select a Route', routes)

# Filter data by selected route
filtered_data = data[data['Route'] == selected_route]

# Calculate the average price for all routes
average_prices = data.groupby('Year')['$Value'].mean().reset_index()

# Plot filtered data for the selected route and compare it with average prices
st.subheader(f'Price Trends for {selected_route} Compared to Average')

fig2, ax2 = plt.subplots(figsize=(10, 6))

# Plot average prices for all routes
ax2.plot(average_prices['Year'], average_prices['$Value'], marker='o', linestyle='--', color='grey', label='Average Price (All Routes)')

# Plot the selected route's prices
sns.lineplot(x='Year', y='$Value', data=filtered_data, ax=ax2, marker='o', label=f'{selected_route} Price')

ax2.set_xlabel('Year', fontsize=12)
ax2.set_ylabel('Price ($)', fontsize=12)
plt.xticks(rotation=90)
plt.title(f'Price Trends for {selected_route} Compared to Average')
plt.legend()
st.pyplot(fig2)

# Explanation:
st.write("**Explanation**: This chart allows you to select a specific flight route and compare its price trend to the average price trend across all routes. The grey dashed line represents the average price across all routes, while the solid line represents the price trend for the selected route.")

# --- Chart 3: Price Distribution by Route (Box Plot) ---
# Create a box plot showing price distribution by year for the selected route
st.subheader(f'Price Distribution for {selected_route} (Yearly Distribution)')

fig3, ax3 = plt.subplots(figsize=(10, 6))
sns.boxplot(x='Year', y='$Value', data=filtered_data, ax=ax3)
ax3.set_xlabel('Year', fontsize=12)
ax3.set_ylabel('Price ($)', fontsize=12)
plt.xticks(rotation=90)
plt.title(f'Price Distribution for {selected_route} by Year')
st.pyplot(fig3)

# Explanation:
st.write("**Explanation**: The box plot shows the distribution of flight prices for the selected route over the years. It provides insights into the spread of prices and helps identify any outliers or variations in prices year by year.")

# --- Chart 4: Correlation Between Routes and Prices (Scatter Plot with Color Legend and Group Filter) ---
# Show how price correlates with different routes (via mean prices for each route)
st.subheader('Correlation Between Routes and Prices (Scatter Plot with Grouping)')

# Extracting the starting city of each route
data['Starting City'] = data['Route'].apply(lambda x: x.split('-')[0])

# Adding a dropdown to select a group of routes based on the starting city
starting_cities = data['Starting City'].unique()
selected_city = st.selectbox('Select a Starting City to Filter Routes', starting_cities)

# Filter data to show only routes starting from the selected city
filtered_data_by_city = data[data['Starting City'] == selected_city]

# Calculate the mean price by route for the filtered routes
mean_price_by_route = filtered_data_by_city.groupby('Route')['$Value'].mean().reset_index()

# Calculate the overall average price across all routes
overall_avg_price = data['$Value'].mean()

# Assign a unique color for each route using a colormap
colors = plt.cm.get_cmap('tab20', len(mean_price_by_route))

# Plot the scatter plot with color coding
fig4, ax4 = plt.subplots(figsize=(10, 6))
for i, route in enumerate(mean_price_by_route['Route']):
    route_data = mean_price_by_route[mean_price_by_route['Route'] == route]
    ax4.scatter(route_data['Route'], route_data['$Value'], color=colors(i), label=route, s=100)

# Add the average price line
ax4.axhline(y=overall_avg_price, color='red', linestyle='--', label=f'Overall Avg Price: ${overall_avg_price:.2f}')

ax4.set_xlabel('Route', fontsize=12)
ax4.set_ylabel('Average Price ($)', fontsize=12)
plt.xticks(rotation=90)
plt.title(f'Average Price by Route (Starting from {selected_city})')
plt.grid(True)
plt.tight_layout()

# Add legend (box beside chart) to represent the colors for each route
ax4.legend(title='Routes', bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(fig4)

# Explanation:
st.write(f"**Explanation**: This scatter plot shows the average price for each route starting from {selected_city}, represented by different colors. The red dashed line represents the overall average price across all routes, helping to compare individual routes to the overall trend. The legend on the right helps you recognize which color corresponds to which route.")