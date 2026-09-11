# Power BI Dashboard Specification

Source: `data/retail_sales_clean.csv`

## DAX Measures
```DAX
Total Sales = SUM(retail_sales_clean[Sales])
Total Quantity = SUM(retail_sales_clean[Quantity])
Total Orders = DISTINCTCOUNT(retail_sales_clean[Order_ID])
Average Order Value = DIVIDE([Total Sales],[Total Orders])
```

## Dashboard Visuals
- KPI cards: Total Sales, Total Quantity, Total Orders, Average Order Value
- Line chart: Monthly Sales Trend
- Column chart: Sales by Category
- Bar chart: Sales by Region
- Table: Product, Category, Quantity, Sales
- Slicers: Region, Category and Date

Note: this repository contains a Power BI-ready specification. An actual `.pbix` file must be created in Power BI Desktop if required by the evaluator.