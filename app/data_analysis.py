import pandas as pd
import numpy as np

def load_and_process_data(file_path):
    data = pd.read_csv(file_path)
    data['Order Date'] = pd.to_datetime(data['Order Date'], errors='coerce')
    data['Month'] = data['Order Date'].dt.month
    monthly_sales = data.groupby('Month')['Sales'].sum().reset_index()
    monthly_sales = monthly_sales.sort_values(by='Month').reset_index(drop=True)
    return monthly_sales

def analyze_sales_data(file_path='/path/to/your/sample_orders.csv'):
    monthly_sales = load_and_process_data(file_path)
    january_sales = monthly_sales.loc[monthly_sales['Month'] == 1, 'Sales'].values[0]
    monthly_sales['Growth (%)'] = (monthly_sales['Sales'] - january_sales) / january_sales * 100

    trend = np.polyfit(monthly_sales['Month'], monthly_sales['Growth (%)'], 1)
    trendline_values = np.polyval(trend, monthly_sales['Month'])
    overall_trend = "Increasing" if trendline_values[-1] > trendline_values[0] else "Decreasing"

    top_increase_month = monthly_sales.loc[monthly_sales['Growth (%)'].idxmax()]
    top_decrease_month = monthly_sales[monthly_sales['Month'] != 1].loc[monthly_sales['Growth (%)'].idxmin()]

    return {
        "Overall Trend": overall_trend,
        "Top Increase Month": top_increase_month['Month'],
        "Top Decrease Month": top_decrease_month['Month'],
        "Top Increase Percentage": top_increase_month['Growth (%)'],
        "Top Decrease Percentage": top_decrease_month['Growth (%)']
    }
