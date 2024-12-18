numerical_columns = df.select_dtypes(include=['number'])
correlation_matrix = numerical_columns.corr()
correlation_matrix

import seaborn as sns
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix Heatmap")
plt.show()