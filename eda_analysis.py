
import pandas as pd
import numpy as np
import matplotlib

# Use a non-interactive backend for reliable image saving
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================
# 1. LOAD DATASET
# ==========================================

df = pd.read_csv("supermarket_sales.csv")

print("\nDATASET LOADED SUCCESSFULLY!")

# ==========================================
# 2. DISPLAY FIRST FIVE ROWS
# ==========================================

print("\nFIRST FIVE ROWS:")
print(df.head())

# ==========================================
# 3. DISPLAY LAST FIVE ROWS
# ==========================================

print("\nLAST FIVE ROWS:")
print(df.tail())

# ==========================================
# 4. DATASET INFORMATION
# ==========================================

print("\nDATASET INFORMATION:")
df.info()

# ==========================================
# 5. DATASET SHAPE
# ==========================================

print("\nDATASET SHAPE:")
print(df.shape)

print("\nNUMBER OF ROWS:", df.shape[0])
print("NUMBER OF COLUMNS:", df.shape[1])

# ==========================================
# 6. COLUMN NAMES
# ==========================================

print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# ==========================================
# 7. CHECK MISSING VALUES
# ==========================================

print("\nMISSING VALUES:")
print(df.isnull().sum())

print("\nTOTAL MISSING VALUES:")
print(df.isnull().sum().sum())

# ==========================================
# 8. CHECK DUPLICATE RECORDS
# ==========================================

print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# ==========================================
# 9. STATISTICAL SUMMARY
# ==========================================

print("\nNUMERICAL STATISTICAL SUMMARY:")
print(df.describe())

# ==========================================
# 10. CATEGORICAL DATA SUMMARY
# ==========================================

print("\nCATEGORICAL DATA SUMMARY:")
categorical_df = df.select_dtypes(include=["object", "str"])
print(categorical_df.describe())

# ==========================================
# 11. MEAN, MEDIAN AND MODE
# ==========================================

numeric_df = df.select_dtypes(include=np.number)

print("\nMEAN:")
print(numeric_df.mean())

print("\nMEDIAN:")
print(numeric_df.median())

print("\nMODE:")
print(numeric_df.mode().iloc[0])

# ==========================================
# 12. STANDARD DEVIATION
# ==========================================

print("\nSTANDARD DEVIATION:")
print(numeric_df.std())

print("\nDATASET EXPLORATION COMPLETED!")

# ==========================================
# 13. CREATE PLOTS FOLDER
# ==========================================

os.makedirs("plots", exist_ok=True)

sns.set_theme(style="whitegrid")

# ==========================================
# 14. HISTOGRAMS
# ==========================================

fig, axes = plt.subplots(2, 2, figsize=(12, 8))

columns = ["Unit price", "Quantity", "Total", "Rating"]

for ax, column in zip(axes.flatten(), columns):
    sns.histplot(
        data=df,
        x=column,
        bins=20,
        kde=True,
        ax=ax
    )
    ax.set_title(f"Distribution of {column}")

fig.suptitle("Distribution of Numerical Features", fontsize=16)
fig.tight_layout()

fig.savefig("plots/histograms.png", format="png", dpi=300)
plt.close(fig)

print("\nHISTOGRAMS SAVED SUCCESSFULLY!")

# ==========================================
# 15. BOXPLOTS
# ==========================================

fig, ax = plt.subplots(figsize=(10, 6))

sns.boxplot(
    data=df[columns],
    ax=ax
)

ax.set_title("Boxplot of Numerical Features")
ax.set_xlabel("Features")
ax.set_ylabel("Values")

fig.tight_layout()
fig.savefig("plots/boxplots.png", format="png", dpi=300)
plt.close(fig)

print("\nBOXPLOTS SAVED SUCCESSFULLY!")

# ==========================================
# 16. CORRELATION HEATMAP
# ==========================================

fig, ax = plt.subplots(figsize=(12, 8))

correlation = numeric_df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    ax=ax
)

ax.set_title("Correlation Heatmap")

fig.tight_layout()
fig.savefig("plots/correlation_heatmap.png", format="png", dpi=300)
plt.close(fig)

print("\nCORRELATION HEATMAP SAVED SUCCESSFULLY!")

# ==========================================
# 17. SALES BY PRODUCT LINE
# ==========================================

fig, ax = plt.subplots(figsize=(11, 6))

sns.barplot(
    data=df,
    x="Product line",
    y="Total",
    estimator="sum",
    errorbar=None,
    ax=ax
)

ax.set_title("Total Sales by Product Line")
ax.set_xlabel("Product Line")
ax.set_ylabel("Total Sales")
ax.tick_params(axis="x", rotation=30)

fig.tight_layout()
fig.savefig("plots/sales_by_product_line.png", format="png", dpi=300)
plt.close(fig)

print("\nSALES BY PRODUCT LINE SAVED SUCCESSFULLY!")

# ==========================================
# 18. FINAL MESSAGE
# ==========================================

print("\nALL VISUALIZATIONS GENERATED SUCCESSFULLY!")
print("\nTASK 2 COMPLETED SUCCESSFULLY!")
print("\nCheck the plots folder for all generated graphs.")
