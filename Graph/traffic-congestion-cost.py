import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file
df = pd.read_excel('/statistic_id1305426_cost-per-driver-of-traffic-congestions-in-the-us-by-urban-area-2019.xlsx', sheet_name="Data", skiprows=4)

# Clean up the data
cities = df['Unnamed: 1'].dropna()  # Get city names, drop any NaN values
costs = df['Unnamed: 2'].dropna()  # Get cost values, drop any NaN values

# Create visualization
plt.figure(figsize=(12, 8))

# Create horizontal bar chart
plt.barh(cities, costs, color='#e41a1c')  # Changed color to red to represent costs

# Customize the graph
plt.title('Cost per Driver of Traffic Congestion in US Urban Areas (2019)', fontsize=14, pad=20)
plt.xlabel('Cost per Driver ($)', fontsize=12)
plt.ylabel('Urban Area', fontsize=12)

# Add value labels on the bars
for i, v in enumerate(costs):
    plt.text(v + 50, i, f'${int(v):,}', va='center')

# Adjust layout and style
plt.margins(x=0.1)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Format the x-axis to show dollar amounts
plt.gca().xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${int(x):,}'))

# Adjust figure size to fit content
plt.subplots_adjust(left=0.25, right=0.9, top=0.9, bottom=0.1)

# Add a light gray background grid
plt.grid(True, axis='x', alpha=0.3)

# Show the plot
plt.show()
