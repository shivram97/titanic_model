import pandas as pd

def read_dataset(file_path:str, format :str="csv"):
    if format=="csv":
        return pd.read_csv(file_path)
    elif(format=="excel"):
        return pd.read_excel(file_path)
    else:
        with open(file_path,"r") as f:
            return f.read()