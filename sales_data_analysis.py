import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

def preprocess_data(df):
    # Convert InvoiceDate to datetime
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def aggregate_sales_data(df):
    # Aggregate sales data by month
    df['InvoiceMonth'] = df['InvoiceDate'].dt.to_period('M')
    numeric_df = df.select_dtypes(include=[np.number])
    monthly_sales = numeric_df.groupby(df['InvoiceMonth']).sum()['Quantity']
    return monthly_sales

def analyze_trends(monthly_sales):
    # Ensure monthly_sales is a pandas Series with a datetime index
    monthly_sales.index = monthly_sales.index.to_timestamp()

    # Plot sales trends over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x=monthly_sales.index, y=monthly_sales.values)
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Quantity Sold')
    plt.savefig('monthly_sales_trends.png')
    plt.show()

    # Highlight outliers on the trend line
    outliers = detect_outliers(monthly_sales)
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=outliers.index, y=outliers.values, color='red', label='Outliers')
    plt.title('Outliers in Monthly Sales Data')
    plt.xlabel('Month')
    plt.ylabel('Total Quantity Sold')
    plt.legend()
    plt.savefig('outliers_in_monthly_sales.png')
    plt.show()

def detect_outliers(monthly_sales):
    # Detect outliers using the IQR method
    Q1 = monthly_sales.quantile(0.25)
    Q3 = monthly_sales.quantile(0.75)
    IQR = Q3 - Q1
    outliers = monthly_sales[(monthly_sales < (Q1 - 1.5 * IQR)) | (monthly_sales > (Q3 + 1.5 * IQR))]
    return outliers

if __name__ == "__main__":
    # Load the cleaned data
    data_file_path = "cleaned_online_retail_data.csv"
    df = load_data(data_file_path)

    # Preprocess the data
    df = preprocess_data(df)

    # Aggregate sales data
    monthly_sales = aggregate_sales_data(df)

    # Analyze sales trends
    analyze_trends(monthly_sales)

    # Detect outliers
    outliers = detect_outliers(monthly_sales)
    print("Outliers detected in monthly sales data:")
    print(outliers)
