import matplotlib.pyplot as plt
import pandas as pd

# Read the Excel file
df = pd.read_excel('/content/drive/My Drive/Colab Notebooks/statistic_id1305446_most-congested-urban-area-in-the-us-2019.xlsx', sheet_name="Data", skiprows=4)

# Clean up the data
cities = df['Unnamed: 1'].dropna()  # Get city names, drop any NaN values
congestion = df['Unnamed: 2'].dropna()  # Get congestion values, drop any NaN values

# Create visualization
plt.figure(figsize=(10, 6))  # Reduced figure size to avoid the dimension error

# Create horizontal bar chart
plt.barh(cities, congestion, color='#2c7fb8')

# Customize the graph
plt.title('Hours Lost in Congestion in the United States in 2019', fontsize=12)
plt.xlabel('Hours lost in congestion', fontsize=10)
plt.ylabel('Urban Area', fontsize=10)

# Add value labels on the bars
for i, v in enumerate(congestion):
   plt.text(v + 0.5, i, f'{int(v)}', va='center')

# Adjust layout
plt.margins(x=0.1)
plt.grid(axis='x', linestyle='--', alpha=0.7)

# Adjust figure size to fit content
plt.gcf().set_size_inches(10, 6)
plt.subplots_adjust(left=0.2, right=0.9, top=0.9, bottom=0.1)

# Show the plot
plt.show()