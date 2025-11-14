import pandas as pd
import os

# Load the dataset
df = pd.read_csv("/Users/mrarnav69/Documents/BizLink V1/data/raw/marketing_and_product_performance.csv")

# Replace missing values with the average for numerical columns
numerical_columns = df.select_dtypes(include=['number']).columns
for col in numerical_columns:
    df[col].fillna(df[col].mean(), inplace=True)

# Remove duplicate rows
df = df.drop_duplicates()

# Standardize categorical values (e.g., ensure consistent capitalization)
categorical_columns = df.select_dtypes(include=['object']).columns
for col in categorical_columns:
    df[col] = df[col].str.strip().str.lower()

# Filter rows based on specific conditions (example: filter out rows with negative values in a column)
if 'sales' in df.columns:
    df = df[df['sales'] >= 0]

# Normalize numerical columns (min-max scaling)
numerical_columns = df.select_dtypes(include=['number']).columns
for col in numerical_columns:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

# Save the cleaned and normalized dataset
output_dir = "/Users/mrarnav69/Documents/BizLink V1/data/preprocessed"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "cleaned_marketing_and_product_performance.csv")
df.to_csv(output_file, index=False)

print(f"Cleaned and normalized data saved to {output_file}")

