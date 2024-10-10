import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

df = pd.read_csv("sp500_esg_data.csv")

financials_df = df[df["GICS Sector"] == "Financials"]

# E-Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=financials_df, x="environmentScore", y="totalEsg")

sns.regplot(
    data=financials_df, x="environmentScore", y="totalEsg", scatter=False, color="red"
)

plt.title(
    "Correlation between Environmental Score and Total ESG Score in Financials Sector"
)
plt.xlabel("Environmental Score")
plt.ylabel("Total ESG Score")

correlation = financials_df["environmentScore"].corr(financials_df["totalEsg"])
slope, intercept, r_value, p_value, std_err = stats.linregress(
    financials_df["environmentScore"], financials_df["totalEsg"]
)

plt.text(
    0.05,
    0.95,
    f"Correlation: {correlation:.2f}\nR-squared: {r_value**2:.2f}",
    transform=plt.gca().transAxes,
    verticalalignment="top",
)

plt.tight_layout()
plt.show()

# S-Score
plt.figure(figsize=(10, 6))
sns.scatterplot(data=financials_df, x="socialScore", y="totalEsg")

sns.regplot(
    data=financials_df, x="socialScore", y="totalEsg", scatter=False, color="red"
)

plt.title("Correlation between Social Score and Total ESG Score in Financials Sector")
plt.xlabel("Social Score")
plt.ylabel("Total ESG Score")

correlation = financials_df["socialScore"].corr(financials_df["totalEsg"])
slope, intercept, r_value, p_value, std_err = stats.linregress(
    financials_df["socialScore"], financials_df["totalEsg"]
)

plt.text(
    0.05,
    0.95,
    f"Correlation: {correlation:.2f}\nR-squared: {r_value**2:.2f}",
    transform=plt.gca().transAxes,
    verticalalignment="top",
)

plt.tight_layout()
plt.show()

plt.figure(figsize=(10, 6))
sns.scatterplot(data=financials_df, x="governanceScore", y="totalEsg")

sns.regplot(
    data=financials_df, x="governanceScore", y="totalEsg", scatter=False, color="red"
)

plt.title(
    "Correlation between Governance Score and Total ESG Score in Financials Sector"
)
plt.xlabel("Governance Score")
plt.ylabel("Total ESG Score")

correlation = financials_df["governanceScore"].corr(financials_df["totalEsg"])
slope, intercept, r_value, p_value, std_err = stats.linregress(
    financials_df["governanceScore"], financials_df["totalEsg"]
)

plt.text(
    0.05,
    0.95,
    f"Correlation: {correlation:.2f}\nR-squared: {r_value**2:.2f}",
    transform=plt.gca().transAxes,
    verticalalignment="top",
)

plt.tight_layout()
plt.show()
