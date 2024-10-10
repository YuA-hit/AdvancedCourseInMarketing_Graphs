import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("sp500_esg_data.csv")

sectors = [
    "Financials",
    "Industrials",
    "Information Technology",
    "Health Care",
    "Consumer Discretionary",
]

sector_data = {sector: df[df["GICS Sector"] == sector] for sector in sectors}

# E-Score
plt.figure(figsize=(12, 8))
for sector, data in sector_data.items():
    plt.scatter(data["totalEsg"], data["environmentScore"], label=sector, alpha=0.7)

plt.title("Environment Score vs Total ESG Score by GICS Sector")
plt.xlabel("Total ESG Score")
plt.ylabel("Environment Score")
plt.legend()

plt.grid(True, linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()


# S-Score
plt.figure(figsize=(12, 8))

for sector, data in sector_data.items():
    plt.scatter(data["totalEsg"], data["socialScore"], label=sector, alpha=0.7)

plt.title("Social Score vs Total ESG Score by GICS Sector")
plt.xlabel("Total ESG Score")
plt.ylabel("Social Score")
plt.legend()

plt.grid(True, linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()

# G-Score
plt.figure(figsize=(12, 8))

for sector, data in sector_data.items():
    plt.scatter(data["totalEsg"], data["governanceScore"], label=sector, alpha=0.7)

plt.title("Governance Score vs Total ESG Score by GICS Sector")
plt.xlabel("Total ESG Score")
plt.ylabel("Governance Score")
plt.legend()

plt.grid(True, linestyle="--", alpha=0.7)

plt.tight_layout()
plt.show()
