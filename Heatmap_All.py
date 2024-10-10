import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("sp500_esg_data.csv")

columns_of_interest = ["environmentScore", "socialScore", "governanceScore", "totalEsg"]

correlation_matrix = df[columns_of_interest].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm", vmin=-1, vmax=1, center=0)

plt.title("Correlation Heatmap of ESG Scores")

plt.tight_layout()
plt.show()

print("Correlation Matrix:")
print(correlation_matrix)

print(f"\nNumber of data points: {len(df)}")
