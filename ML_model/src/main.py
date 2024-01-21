import os 
import pandas as pd
import numpy as np

from util.io_util import read_dataset
from constant import *
from preprocessing.process import *
from training.train import *
from training.evaluation import *
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

## cache can be used to store the processed CODE AND REPEATABLE  CODE
#read data
logging.info("reading data")
df = read_dataset(file_path=loan_default_csv,format="csv")
logging.info("reading data complete")

print(df.head())
logging.info("Cleaning dataset")
#clean the data
#1.remove the unique columns
df = clean_dataframe(df,0.4)
logging.info("Perform missing imputation")

df = missing_imputation(df)
print(df.head())

logging.info("Encoding categorical data")

df,label_encoders= encode_df(df)

print(df)
print(label_encoders)

logging.info("splitting dataset")

X_train, X_test, y_train, y_test = training_split(df,predict_col)

logging.info("Training model")

model = train(X_train,y_train)

logging.info("Evaluating model")

metrics = evaluate_classification(model.predict(X_test),y_test)

print(metrics)