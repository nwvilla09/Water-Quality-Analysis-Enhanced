import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to database
conn = sqlite3.connect('water_quality.db')

# Query
query = '''
    WITH MonthlyQuality AS (
        SELECT 
            strftime('%Y-%m', Sample_Date) AS Month,
            Potability,
            AVG(COALESCE(ph, 7.0)) AS avg_ph,
            AVG(COALESCE(Hardness, 196.0)) AS avg_hardness,
            COUNT(*) AS sample_count
        FROM water_quality
        GROUP BY Month, Potability
    )
    SELECT 
        mq.Month,
        mq.Potability,
        mq.avg_ph,
        mq.avg_hardness,
        mq.sample_count,
        SUM(tc.Cost_Per_Sample * mq.sample_count) AS Total_Cost
    FROM MonthlyQuality mq
    LEFT JOIN treatment_costs tc ON mq.Potability = tc.Potability
    GROUP BY mq.Month, mq.Potability
    ORDER BY mq.Month, mq.Potability
'''
df = pd.read_sql_query(query, conn)
print(df.groupby('Potability')['Total_Cost'].sum())  # Debug: $1,598,400 (0), $127,800 (1)
df.to_csv('advanced_water_quality_report.csv', index=False)

# Visualization 1: Monthly Average pH (Bar)
df_pivot_ph = df.pivot(index='Month', columns='Potability', values='avg_ph')
df_pivot_ph.plot(kind='bar', color=['red', 'blue'], width=0.8)
plt.title('Monthly Average pH by Potability')
plt.xlabel('Month (YYYY-MM)')
plt.ylabel('Average pH')
plt.legend(['Not Potable (0)', 'Potable (1)'])
plt.ylim(6.0, 8.0)
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_ph_bar.png')
plt.close()

# Visualization 2: Annual Treatment Costs (Pie)
df_pie_data = df.groupby('Potability')['Total_Cost'].sum().reset_index()
total_costs = {0: df_pie_data.loc[df_pie_data['Potability'] == 0, 'Total_Cost'].iloc[0],
               1: df_pie_data.loc[df_pie_data['Potability'] == 1, 'Total_Cost'].iloc[0]}
plt.pie(df_pie_data['Total_Cost'], labels=None, colors=['red', 'blue'],
        autopct=lambda pct: f'{pct:.0f}% (${int(total_costs[0] if pct > 50 else total_costs[1]):,})',
        textprops={'color': 'white', 'weight': 'bold', 'bbox': dict(facecolor='black', edgecolor='none', boxstyle='round,pad=0.5')})
plt.legend(['Not Potable (0)', 'Potable (1)'], loc='best')
plt.title('Annual Treatment Costs by Potability')
plt.tight_layout()
plt.savefig('monthly_cost_pie.png')
plt.close()

# Visualization 3: Monthly Sample Count (Scatter)
df_pivot_count = df.pivot(index='Month', columns='Potability', values='sample_count')
plt.scatter(df_pivot_count.index, df_pivot_count[0], color='red', label='Not Potable (0)')
plt.scatter(df_pivot_count.index, df_pivot_count[1], color='blue', label='Potable (1)')
plt.title('Monthly Sample Count by Potability')
plt.xlabel('Month (YYYY-MM)')
plt.ylabel('Sample Count')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_sample_scatter.png')
plt.close()

# Visualization 4: Monthly Average Hardness (Line)
df_pivot_hardness = df.pivot(index='Month', columns='Potability', values='avg_hardness')
df_pivot_hardness.plot(kind='line', marker='o', color=['red', 'blue'])
plt.title('Monthly Average Hardness by Potability')
plt.xlabel('Month (YYYY-MM)')
plt.ylabel('Average Hardness (mg/L)')
plt.legend(['Not Potable (0)', 'Potable (1)'])
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('monthly_hardness_line.png')
plt.close()

conn.close()