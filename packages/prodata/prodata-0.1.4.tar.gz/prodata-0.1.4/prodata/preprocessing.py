import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder



def impute_missing_data(df, exclude_cols=None):
    if exclude_cols is None:
        exclude_cols = []

    for col in df.columns:
        if col in exclude_cols:
            continue  # Skip columns specified for exclusion

        if pd.api.types.is_numeric_dtype(df[col]):
            # Impute missing values in numeric columns
            if df[col].isnull().any():
                # Calculate IQR
                Q1 = df[col].quantile(0.25)
                Q3 = df[col].quantile(0.75)
                IQR = Q3 - Q1

                # Determine outliers based on IQR
                lower_bound = Q1 - 1.5 * IQR
                upper_bound = Q3 + 1.5 * IQR

                # Impute with median if values are outside the bounds
                if (df[col] < lower_bound).any() or (df[col] > upper_bound).any():
                    median_value = df[col].median()
                    df[col] = df[col].fillna(median_value)
                else:
                    mean_value = df[col].mean()
                    df[col] = df[col].fillna(mean_value)

        elif isinstance(df[col].dtype, pd.CategoricalDtype) or pd.api.types.is_object_dtype(df[col]):
            # Impute missing values in object (string) or categorical columns with mode
            mode_value = df[col].mode().iloc[0]
            df[col] = df[col].fillna(mode_value)

        elif pd.api.types.is_datetime64_any_dtype(df[col]):
            # Skip imputation for datetime columns
            continue

        else:
            # Handle other types if needed (for future extension)
            pass

    return df



# def treat_outliers(df):
#     # Capping method
#     for col in df.select_dtypes(include=['number']).columns:
#         Q1 = df[col].quantile(0.25)
#         Q3 = df[col].quantile(0.75)
#         IQR = Q3 - Q1
#         lower_bound = Q1 - 1.5 * IQR
#         upper_bound = Q3 + 1.5 * IQR
        
        
#         df[col] = df[col].apply(lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x))
#         # Add other outlier treatment methods as needed
#     return df


def treat_outliers(df, exclude_cols=None):
    if exclude_cols is None:
        exclude_cols = []

    for col in df.select_dtypes(include=['number']).columns:
        if col in exclude_cols:
            continue  # Skip columns specified for exclusion
        
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        df[col] = df[col].apply(lambda x: lower_bound if x < lower_bound else (upper_bound if x > upper_bound else x))
        # Add other outlier treatment methods as needed
    
    return df




# def encode_categorical_columns(df, method='label'):
#     categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
#     if method == 'label':
#         label_encoder = LabelEncoder()
#         for col in categorical_cols:
#             df[col + '_encoded'] = label_encoder.fit_transform(df[col].astype(str))
    
#     elif method == 'one-hot':
#         df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
#     return df

def encode_categorical_columns(df, method='label', exclude_cols=None):
    df = df.copy()  # Make a copy to avoid modifying the original DataFrame
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    
    if method not in ['label', 'one-hot']:
        raise ValueError("Invalid method. Choose either 'label' or 'one-hot'.")
    
    if exclude_cols is None:
        exclude_cols = []
    
    if method == 'label':
        label_encoder = LabelEncoder()
        for col in categorical_cols:
            if col not in exclude_cols:
                encoded_col = col + '_encoded'
                df[encoded_col] = label_encoder.fit_transform(df[col].astype(str))
                # Drop the original column after encoding
                df.drop(columns=[col], inplace=True)
    
    elif method == 'one-hot':
        categorical_cols = [col for col in categorical_cols if col not in exclude_cols]
        df = pd.get_dummies(df, columns=categorical_cols, drop_first=True)
    
    return df





def draw_boxplots(df):
    # Get numerical columns
    numerical_cols = df.select_dtypes(include=['number']).columns
    
    # Plot boxplots for each numerical column
    for col in numerical_cols:
        plt.figure(figsize=(8, 6))  # Adjust the figure size as needed
        sns.boxplot(x=df[col])
        plt.title(f'Boxplot of {col}')
        plt.show()
