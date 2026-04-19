# E-commerce Customer Orders Analysis

## Overview

This project focuses on data analysis and transformation using Python and pandas.
The goal is to process a small customer orders dataset and extract meaningful business insights such as customer spending behavior and sales distribution by country.

---

## Objectives

* Load and explore customer order data
* Create calculated metrics for analysis
* Organize and structure the dataset
* Identify top-performing customers
* Analyze sales performance by country

---

## Data Processing Steps

* Loaded dataset using `pandas`
* Created a new column:

  * `total = quantity * price`
* Sorted dataset by:

  * `country` (grouped view)
  * `order_date` (chronological order)
* Grouped data by `country` to inspect orders
* Aggregated data using `groupby` to calculate:

  * Total spending per customer
  * Total revenue per country

---

## Exploratory Data Analysis

* Identified the highest-spending customer
* Retrieved the country of the top customer
* Calculated total revenue by country
* Inspected order distribution across countries
* Organized data for better readability and interpretation

---

## Tools Used

* Python 🐍
* pandas 📊
* pathlib 📁

---

## Key Insights

* A single customer can contribute significantly to total revenue
* Revenue distribution varies across countries
* Grouping by customer reveals spending patterns
* Sorting by date helps understand order flow over time
* Creating derived metrics (`quantity × price`) is essential for analysis

---

## Learning Outcomes

* Strengthened data manipulation skills with pandas
* Learned how to group and aggregate data effectively
* Practiced extracting insights from structured datasets
* Improved ability to organize and present data clearly

---

## Conclusion

This project demonstrates how basic data processing and aggregation techniques can transform raw transactional data into useful business insights.
