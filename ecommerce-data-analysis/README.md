# E-commerce Data Analysis Project

## Overview
This project focuses on data wrangling and exploratory data analysis using Python and pandas.  
The goal is to clean a simple e-commerce dataset and extract basic business insights such as revenue per country and product-level patterns.

---

## Objectives
- Load and inspect raw e-commerce order data  
- Remove duplicate records  
- Create calculated fields for analysis  
- Sort and structure data for better readability  
- Aggregate data to extract business insights  

---

## Data Processing Steps
- Loaded dataset using `pandas`
- Removed duplicate rows to ensure data quality
- Created a new column:
  - `total = quantity * price`
- Sorted dataset by:
  - `country` (A → Z)
  - `price` (Low → High)
- Aggregated data using `groupby` to calculate:
  - Total revenue per country

---

## Exploratory Data Analysis
- Calculated total revenue per country using aggregation
- Analyzed product price distribution through sorting
- Compared countries based on total sales
- Performed basic dataset structure inspection

---

## Tools Used
- Python 🐍
- pandas 📊
- pathlib 📁

---

## Key Insights
- Portugal shows strong total revenue compared to other countries  
- Product prices vary significantly across categories  
- Aggregation by country helps identify regional performance differences  
- Simple feature engineering (`quantity × price`) is essential for meaningful analysis  

---

## Learning Outcomes
- Improved understanding of pandas data manipulation  
- Practiced grouping and aggregation techniques  
- Learned how to transform raw data into insights  
