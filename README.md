# AI/ML Internship – Task 2
## Exploratory Data Analysis on Supermarket Sales

### Project Overview
This project performs Exploratory Data Analysis (EDA) on a supermarket sales dataset using Python. The objective is to understand sales patterns, explore numerical and categorical variables, calculate statistical measures, and visualize important business insights.

### Dataset Information
- Dataset: Supermarket Sales
- Total Records: 1000
- Total Columns: 17
- Missing Values: 0
- Duplicate Records: 0

### Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

### Tasks Performed
1. Dataset loading and inspection
2. Displaying first and last five records
3. Dataset information and shape analysis
4. Checking column names
5. Missing value detection
6. Duplicate record detection
7. Numerical statistical summary
8. Categorical data analysis
9. Mean, median, and mode calculation
10. Standard deviation calculation
11. Data visualization
12. Correlation analysis
13. Sales analysis by product line

### Visualizations
The project generates four visualizations:

1. Histograms – Distribution of numerical features.
2. Boxplots – Identification of data distribution and outliers.
3. Correlation Heatmap – Relationships between numerical variables.
4. Sales by Product Line – Comparison of total sales across product categories.

### Key Findings
- The dataset contains 1000 records without missing or duplicate values.
- Average unit price is approximately 55.67.
- Average quantity per transaction is 5.51.
- Average total transaction value is approximately 322.97.
- Average customer rating is approximately 6.97.
- Gross margin percentage is consistently 4.761905%.

### Project Structure
```text
AI-ML-Task-2/
│
├── plots/
│   ├── histograms.png
│   ├── boxplots.png
│   ├── correlation_heatmap.png
│   └── sales_by_product_line.png
│
├── supermarket_sales.csv
├── eda_analysis.py
├── requirements.txt
├── README.md
└── .gitignore
```

### How to Run the Project

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Python script:

```bash
python eda_analysis.py
```

### Conclusion
This project demonstrates how Python-based Exploratory Data Analysis can be used to inspect supermarket sales data, understand statistical patterns, identify outliers, and visualize relationships between different variables.

**Task 2 – Completed**
