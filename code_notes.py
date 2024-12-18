numerical_columns = df.select_dtypes(include=['number'])
correlation_matrix = numerical_columns.corr()
correlation_matrix

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()


---

# First, create a mapping from each 'ModelFamily' to its predecessor's 'phone_series'
# This will allow us to look up the predecessor's 'phone_series' for each model family

# Create a dictionary mapping ModelFamily to the phone_series of its predecessor
predecessor_phone_series_map = df.dropna(subset=['phone_series', 'predecessor']).groupby('model_family')['phone_series'].first().to_dict()

# Now, we can use this map to fill the NaN values in 'phone_series' for rows with a predecessor
# If the row has NaN in 'phone_series', we replace it with the 'phone_series' of the predecessor's ModelFamily

# Define a function to impute Phone Series using the predecessor's phone_series
def impute_phone_series(row):
    if pd.isna(row['phone_series']) and row['predecessor'] in predecessor_phone_series_map:
        # Use predecessor's phone_series from the map
        return predecessor_phone_series_map[row['predecessor']]
    return row['phone_series']

# Apply the function to impute missing phone_series
df['phone_series'] = df.apply(impute_phone_series, axis=1)