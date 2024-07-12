prodata

prodata is a Python library designed to streamline common data preprocessing tasks, making it easier for data scientists and analysts to prepare their datasets for analysis and modeling. This library provides functions to handle missing data, treat outliers, encode categorical variables, and visualize data distribution using boxplots.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Installation:
pip install prodata
from prodata.preprocessing import impute_missing_data, treat_outliers, encode_categorical_columns, draw_boxplots

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Usage:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from prodata.preprocessing import impute_missing_data, treat_outliers, encode_categorical_columns, draw_boxplots

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Functions:

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. impute_missing_data(df, exclude_cols = ['A'])... for an example
Purpose: Imputes missing values in a DataFrame. (Numerical and categorical columns)

Parameters:
df (DataFrame): Input DataFrame with missing values. Any columns that do not wish to be treated, can be left out and then the
dataframe can be put as an input parameter.

exclude_cols = this parameter helps to exclude columns that needs to be kept untreated. Input is in the form of a list
for eg, impute_missing_data(df, exclude_cols = ['Age'])

Usage: Handles missing data by imputing based on column type (numeric, categorical). Datetime datatype is
not treated by default. Whichever column needs to remain untreated, can be mentioned in the form of a list in the parameter of the function. For numeric datatype - if column has outliers, median is used to impute missing data, if not, mean is used. 
For categorical columns, mode of the column is used to impute missing data within that particular column.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

2. treat_outliers(df)
Purpose: Treats outliers in numerical columns using the capping method.

Parameters:
df(DataFrame): Input DataFrame. By default, numerical columns are selected to be treated for outliers. 

exclude_cols = (Selection of columns): By default, all the columns from input dataframe are treated. However, whichever columns need to be left untreated should be mentioned in the function parameters as a list. 

eg: df = treat_outliers(df, exclude_cols = ['results'])

Usage: Adjusts extreme values in numerical data to improve robustness in statistical analysis and modeling. Interquartile method is used, where values lower than lower limit are capped to lower limit and values greater than upper limit are capped to upper limit.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

3. encode_categorical_columns(df, method='label', exclude_cols = None)
Purpose: Encodes categorical variables in a DataFrame.

Parameters:
df (DataFrame): Input DataFrame. By default, categorical and columns of data type object are encoded, an input of a subset containing only categorical columns is not required. Object type columns are selected by the fucntions and any columns that are to be excluded from encoding can be mentioned in the parameter of 'exclude_cols'.

exclude_cols = this parameter helps to exclude any columns that are not to be encoded. These columns should be given as an input in the form of a list.

method (str, optional): Method of encoding ('label' for Label Encoding, 'one-hot' for One-Hot Encoding). Default is 'label'.

Usage: Converts categorical variables into numerical representations for machine learning algorithms. Supports both Label Encoding and One-Hot Encoding.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

4. draw_boxplots(df)
Purpose: Visualizes the distribution of numerical data using boxplots. Also for the visusalization of outliers.

Parameters:
df (DataFrame): Numerical columns are selected automatically, no need to input only a subset of dataframe containing numerical columns.

Usage: Generates boxplots for each numerical column in the DataFrame, aiding in understanding data distribution and identifying outliers.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Example:
# Example usage of prodata functions
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [10, 20, None, 40, 50],
    'D': ['A', 'B', 'A', 'C', 'B']
})

# Impute missing data
df = impute_missing_data(df)

# Treat outliers
df = treat_outliers(df)

# Encode categorical columns using Label Encoding
df = encode_categorical_columns(df, method='label', exclude_cols = ['D'])

# Draw boxplots
draw_boxplots(df)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

License:
This project is licensed under the MIT License - see the LICENSE file for details.


Contributing:
Contributions are welcome! Please feel free to submit issues and pull requests.