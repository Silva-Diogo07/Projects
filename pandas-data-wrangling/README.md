# Pandas Data Wrangling Project

## Overview
This project focuses on data wrangling and exploratory data analysis using Python and pandas. The goal is to clean a messy dataset and extract useful insights.

## Objectives
- Load and inspect raw data
- Handle missing and invalid values
- Remove duplicates
- Transform data types
- Perform basic exploratory data analysis (EDA)

## Data Cleaning Steps
- Converted date column to datetime format
- Handled invalid dates by converting them to NaT and removing them
- Removed duplicate rows
- Capped extreme values in the Duration column
- Reset index for clean output

## Exploratory Data Analysis
- Summary statistics using `describe()`
- Grouping data by category
- Correlation between numerical variables
- Identification of most expensive product
- Value counts per category

## Tools Used
- Python
- pandas

## Key Insights
- Some invalid and duplicate data entries were present and cleaned
- Price values showed high variation and outliers
- Tech products tend to have higher prices than Food products
