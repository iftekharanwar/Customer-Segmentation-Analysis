import pandas as pd

def clean_data(df):
    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.fillna(method='ffill').fillna(method='bfill')

    return df

def preprocess_data(file_path):
    # Read the Excel file
    df = pd.read_excel(file_path)

    # Clean the data
    df = clean_data(df)

    return df

if __name__ == "__main__":
    # Example usage
    excel_data_path = "/home/ubuntu/data/Online Retail.xlsx"

    excel_data = preprocess_data(excel_data_path)

    # Save the cleaned data
    excel_data.to_csv("cleaned_online_retail_data.csv", index=False)
