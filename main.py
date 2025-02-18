```python
import csv
import pandas as pd

# 1. Load the dataset
def load_data(path):
    try:
        data = pd.read_csv(path)
        print("Data loaded successfully!")
        return data
    except FileNotFoundError:
        print("File not found. Please check the file path and try again.")

# Load your data
data = load_data('your_data.csv')


# 2. Inspect the dataset
def inspect_data(data):
    print("First 5 rows of data:")
    print(data.head())
    print("\nData info:")
    print(data.info())
    print("\nData description:")
    print(data.describe())

# Inspect your data
inspect_data(data)


# 3. Handle missing values
def handle_missing_values(data):
    print("\nCount of missing values in each column:")
    print(data.isnull().sum())
    data.fillna(data.mean(), inplace=True)
    print("\nMissing values handled.")

# Handle missing values in your data
handle_missing_values(data)


# 4. Encode categorical data
def encode_categorical_data(data):
    categorical_columns = data.select_dtypes(include=['object']).columns
    for col in categorical_columns:
        data[col] = data[col].astype('category').cat.codes
    print("\nCategorical data encoded.")

# Encode categorical data in your data
encode_categorical_data(data)


# 5. Normalize numerical data
def normalize_numerical_data(data):
    numerical_columns = data.select_dtypes(include=['int64', 'float64']).columns
    for col in numerical_columns:
        data[col] = (data[col] - data[col].min()) / (data[col].max() - data[col].min())
    print("\nNumerical data normalized.")

# Normalize numerical data in your data
normalize_numerical_data(data)


# 6. Split the data into training and testing sets
from sklearn.model_selection import train_test_split

def split_data(data, target_column, test_size=0.2):
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    return X_train, X_test, y_train, y_test

# Split your data
# Replace 'target' with your actual target column
X_train, X_test, y_train, y_test = split_data(data, 'target')


# 7. Save the processed data
def save_data(data, path):
    data.to_csv(path, index=False)
    print("\nData saved to " + path)

# Save your processed data
save_data(data, 'processed_data.csv')
```

Цей скрипт виконує основні операції обробки даних: завантажує набір даних, інспектує його, обробляє пропущені значення, кодує категоріальні дані, нормалізує числові дані, розбиває дані на навчальні та тестові набори і зберігає оброблені дані. Перед виконанням цього коду, будь ласка, замініть `'your_data.csv'` та `'target'` на відповідні шлях до вашого файлу та цільову колонку.