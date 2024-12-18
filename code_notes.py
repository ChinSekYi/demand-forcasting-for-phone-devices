---
#TODO: to add in data insights report?
import matplotlib.pyplot as plt

# Convert 'year_month' to datetime and extract 'year'
df['year_month'] = pd.to_datetime(df['year_month'])
df['year'] = df['year_month'].dt.year

# Group by 'year' and 'make', and calculate the average churn rate
agg_df = df.groupby(['year', 'phone_series'], as_index=False)['closing_subs_monthly'].mean()

# Initialize the plot
plt.figure(figsize=(10, 6))

# Group by 'make' and plot each group's average churn rate
for make, group in agg_df.groupby('phone_series'):
    plt.plot(group['year'], group['closing_subs_monthly'], label=make, linewidth=2)

# Add labels, title, and legend
plt.xlabel('Year')
plt.ylabel('Average closing_subs_monthly')
plt.title('Average closing_subs_monthly by Phone Make Over Time')
plt.legend(title='phone_series')

# Improve aesthetics
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()

---
## Chi-square test
Measures the independence between categorical features and the target variable.