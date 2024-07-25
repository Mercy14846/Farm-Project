import pandas as pd

# Load the CSV file
file_path = 'C:/Users/173330/Downloads/Data_Analyst_Assessment_Test.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
data.head(5)

# Check for missing values and data types
missing_values = data.isnull().sum()
data_types = data.dtypes

missing_values_summary = pd.DataFrame({
    'Missing Values': missing_values,
    'Data Type': data_types
})

# Display columns with missing values
missing_values_summary[missing_values_summary['Missing Values'] > 0]

# Drop completely empty or irrelevant columns
data_cleaned = data.drop(columns=['Unnamed: 81'])

# Handle columns with many missing values
threshold = 0.5 * len(data_cleaned)  # If more than 50% of the data is missing, drop the column
data_cleaned = data_cleaned.dropna(axis=1, thresh=threshold)

# Handle remaining missing values by filling with appropriate strategies (e.g., mode for categorical, mean for numerical)
categorical_cols = data_cleaned.select_dtypes(include=['object']).columns
numerical_cols = data_cleaned.select_dtypes(include=['float64', 'int64']).columns

# Fill categorical columns with mode
for col in categorical_cols:
    data_cleaned[col] = data_cleaned[col].fillna(data_cleaned[col].mode()[0])

# Fill numerical columns with mean
for col in numerical_cols:
    data_cleaned[col] = data_cleaned[col].fillna(data_cleaned[col].mean())

# Convert date columns to datetime format
date_cols = ['expected_harvest_date']
for col in date_cols:
    data_cleaned[col] = pd.to_datetime(data_cleaned[col], errors='coerce')

# Display the cleaned dataset
data_cleaned.head()

import pandas as pd

# Load the cleaned dataset
data_cleaned = pd.read_csv('C:/Users/173330/Downloads/Data_Analyst_Assessment_Test.csv')

# Summary statistics for numerical columns
numerical_summary = data_cleaned.describe()

# Summary for categorical columns
categorical_cols = data_cleaned.select_dtypes(include=['object']).columns
categorical_summary = data_cleaned[categorical_cols].describe()

print(numerical_summary)
print(categorical_summary)

import matplotlib.pyplot as plt
import seaborn as sns

# List of numerical columns
numerical_cols = data_cleaned.select_dtypes(include=['float64', 'int64']).columns

# Number of numerical columns
num_numerical_cols = len(numerical_cols)

# Calculate the number of rows and columns needed for the subplots
n_cols = 3
n_rows = (num_numerical_cols + n_cols - 1) // n_cols  # This ensures enough rows for all columns

# Visualize distribution of key numerical variables
plt.figure(figsize=(16, 6))

for i, col in enumerate(numerical_cols):
    plt.subplot(n_rows, n_cols, i + 1)
    sns.histplot(data_cleaned[col], kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# Select only numeric columns for the correlation matrix
numeric_data = data_cleaned.select_dtypes(include=['float64', 'int64'])

# Correlation matrix
correlation_matrix = numeric_data.corr()

# Visualize the correlation matrix
plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt

# Ensure your cleaned data is in a DataFrame called 'data_cleaned'

# Create a GeoDataFrame
geometry = [Point(xy) for xy in zip(data_cleaned['longitude'], data_cleaned['latitude'])]
geo_df = gpd.GeoDataFrame(data_cleaned, geometry=geometry)

# Read the Natural Earth shapefile
world = gpd.read_file("C:/Users/173330/OneDrive/Documents/Codeses/Analayis/110m_cultural/ne_110m_admin_0_tiny_countries.shp")

# Plot the geospatial data
ax = world.plot(figsize=(10, 6))
geo_df.plot(ax=ax, markersize=10, color='red', alpha=0.5)
plt.title('Geospatial Distribution of Farms')
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

# Summary statistics for numerical columns
numerical_summary = data_cleaned.describe()

# Summary for categorical columns
categorical_cols = data_cleaned.select_dtypes(include=['object']).columns
categorical_summary = data_cleaned[categorical_cols].describe()

# List of numerical columns
numerical_cols = data_cleaned.select_dtypes(include=['float64', 'int64']).columns

# Number of numerical columns
num_numerical_cols = len(numerical_cols)

# Calculate the number of rows and columns needed for the subplots
n_cols = 3
n_rows = (num_numerical_cols + n_cols - 1) // n_cols  # This ensures enough rows for all columns

# Visualize distribution of key numerical variables
plt.figure(figsize=(16, 6))

for i, col in enumerate(numerical_cols):
    plt.subplot(n_rows, n_cols, i + 1)
    sns.histplot(data_cleaned[col], kde=True)
    plt.title(f'Distribution of {col}')

plt.tight_layout()
plt.show()

# Display summary statistics
numerical_summary, categorical_summary
