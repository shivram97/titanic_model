import pandas as pd
import pdb
from sklearn.preprocessing import LabelEncoder


def clean_dataframe(df:pd.DataFrame , threshold : float=0.4) ->pd.DataFrame:
    """
    Cleans a dataframe by removing columns that have either a high number of unique values or a high number of missing values.

    Parameters:
        df (pd.DataFrame): The input dataframe to be cleaned.
        threshold (float, optional): The threshold value to determine when to remove a column. Defaults to 0.4.

    Returns:
        pd.DataFrame: The cleaned dataframe with the specified columns removed.
    """
    cols_to_remove=[]
    for col in df.columns:
        if len(df[col].unique())/len(df) >= threshold:
            cols_to_remove.append(col)
        elif df[col].isnull().sum()/len(df) >= threshold:
            cols_to_remove.append(col)
    print("Dropping columns: ",cols_to_remove)

    if len(cols_to_remove)>0:
        df=df.drop(cols_to_remove,axis=1)

    return df


def missing_imputation(df):
    """
    Calculates the missing imputations for each column in the given DataFrame.

    Parameters:
        df (DataFrame): The input DataFrame containing the data to be imputed.

    Returns:
        DataFrame: The DataFrame with missing values imputed.
    """
    cols_for_imputation = []

    for col in df.columns:
        if df[col].isnull().sum() > 0:
            cols_for_imputation.append(col)

    # Check if the col is numeric or categorical and perform missing imputation
    for col in cols_for_imputation:
        if df[col].dtype == 'object':
            # Perform categorical missing imputation
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            # Perform numeric missing imputation
            df[col].fillna(df[col].mean(), inplace=True)
    return df


def encode_df(df):
    """
    Generates a dictionary of LabelEncoder objects for each categorical column in the input DataFrame and applies the encoding to the DataFrame.

    Args:
        df (DataFrame): The input DataFrame to encode.

    Returns:
        Tuple[DataFrame, Dict[str, LabelEncoder]]: A tuple containing the encoded DataFrame and a dictionary of LabelEncoder objects for each encoded column.
    """
    cols_to_encode=[]
    for col in df.columns:
        if df[col].dtype == 'object':
            cols_to_encode.append(col)


    print("Columns to encode: ",cols_to_encode)

    res={}

    for col in cols_to_encode:
        le= LabelEncoder()
        df[col]= le.fit_transform(df[col])
        res[col]=le

    return df,res