import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sp500_esg_data.csv")

sector_counts = df["GICS Sector"].value_counts()

plt.figure(figsize=(12, 6))

sector_counts.plot(kind="bar")

plt.title("Frequency of GICS Sectors")
plt.xlabel("GICS Sector")
plt.ylabel("Frequency")
plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()
