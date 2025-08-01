# Enhanced Water Quality Analysis Project

## Overview
This project analyzes water quality data using SQL, Python, Tableau, and Power BI to generate insights into pH levels, treatment costs, sample counts, and hardness for water resource management. The analysis leverages a real-world dataset enhanced with simulated treatment cost data to support decision-making in water quality assessment.

## Dataset
- **Source**: [Water Quality and Potability](https://www.kaggle.com/datasets/adityakadiwal/water-potability) from Kaggle
  - **Description**: A real-world dataset with 3,276 records, including 9 water quality metrics (pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity) and a Potability label (0 = not potable, 1 = potable). This dataset serves as the foundation for analyzing water quality trends.
- **Simulated Data**: The `treatment_costs` table within `water_quality.db` contains simulated data for cost analysis.
  - **Description**: Includes `Potability` (0 or 1) and `Cost_Per_Sample` (e.g., $200.00 per sample as a default value), generated to estimate annual treatment costs ($1,598,400 for Not Potable, $127,800 for Potable). This simulated data enhances the real-world dataset to support water resource management decisions, such as cost allocation and treatment prioritization.

## Files
- `advanced_sql_report.py`: Python script for data processing and visualization.
- `water_quality.db`: SQLite database containing water quality data.
- `advanced_water_quality_report.csv`: Exported data summary.
- `monthly_ph_bar.png`, `monthly_cost_pie.png`, `monthly_sample_scatter.png`, `monthly_hardness_line.png`: Generated visualizations.
- Tableau (`.twb`) and Power BI (`.pbix`) files are available in the repository for download to access pre-built dashboards.
- `water_potability`: Raw dataset file included in the repository for convenience, sourced from the Kaggle dataset.
- `README.md`: Project documentation.

## How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```
3. Ensure `water_quality.db` is in the project directory.
4. Run `advanced_sql_report.py` in Spyder:
   ```bash
   %runfile C:/WaterProject/advanced_sql_report.py --wdir
   ```
5. Open `advanced_water_quality_report.csv` for raw data.
6. Download and open the `.twb` or `.pbix` files from the repository to explore Tableau or Power BI dashboards.

## Skills Demonstrated
- **SQL**: Use of CTEs, GROUP BY, and LEFT JOINs for aggregating water quality metrics and treatment costs.
- **Python**: Data manipulation with pandas, advanced visualization with matplotlib (bar, pie, scatter, line charts).
- **Reporting**: Automated CSV reports and multi-visualization outputs for management insights.
- **Data Integration**: Combining real-world data with simulated treatment costs for water resource management analysis.
- **Visualization Tools**: Integration with Tableau and Power BI for interactive dashboards.

## Example Output
The report (`advanced_water_quality_report.csv`) summarizes monthly average pH, hardness, sample counts, and annual treatment costs by potability. Visualizations include:
- `monthly_ph_bar.png`: Bar chart of monthly pH by potability.
- `monthly_cost_pie.png`: Pie chart of annual treatment costs (e.g., "93% ($1,598,400)" for Not Potable, "7% ($127,800)" for Potable).
- `monthly_sample_scatter.png`: Scatter plot of monthly sample counts.
- `monthly_hardness_line.png`: Line chart of monthly hardness by potability.

## Future Improvements
- Add time-series analysis with enhanced timestamp data.
- Incorporate predictive modeling for water quality trends.
- Expand Power BI dashboards with real-time data integration.

## Updates
- Added pie chart for treatment costs with custom labels, improving financial insight.
- Implemented multi-visualization support (bar, pie, scatter, line) for comprehensive reporting.
- Enhanced SQL query with CTE for better data aggregation.

## License
MIT License - See LICENSE file for details.