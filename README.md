# Week 6 Final Data Analytics Project
**Student:** Addepalli Durga Charan

## Retail Sales Analysis
End-to-end project covering data preparation, EDA, visualization, Power BI planning, and business recommendations.

### Dataset
The project uses a retail sales dataset with order date, customer, product, category, region, quantity, unit price, discount and sales.

### Cleaning
- Removed duplicate records
- Filled missing Region with `Unknown`
- Replaced invalid Quantity values with the median
- Recalculated missing Sales values
- Converted Date to datetime

### EDA & Visualization
The analysis covers descriptive statistics, category and regional performance, monthly sales trends, product performance, sales distribution, and correlation analysis.

### Power BI
See `powerbi/dashboard_specification.md` for recommended DAX measures, visuals and slicers. An actual `.pbix` file is not included in this repository package.

### Recommendations
1. Prioritize high-revenue categories.
2. Investigate weaker regions and product segments.
3. Use monthly trends for inventory and promotion planning.
4. Monitor discounts alongside sales volume and profitability.
