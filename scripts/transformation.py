import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer
import logging
from logging.handlers import TimedRotatingFileHandler

class DataTransformer:
    def __init__(self) -> None:
        logging.basicConfig(filename="../logs/clean.log", level=logging.INFO, format="time: %(asctime)s, function: %(funcName)s, module: %(name)s, message: %(message)s \n")
        

    def cat_num(self, df):
        categorical_columns = df.select_dtypes(include='object')
        numerical_columns = df.select_dtypes(exclude='object')
        logging.info("differentiate catagorical vs numerical")
        return categorical_columns, numerical_columns

    
    def cat_labeler(self, df, cat_cols):
        for column in cat_cols:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
        
        logging.info("label category")
        return df


    def scaler(self, df):
        scaling = MinMaxScaler()
        df[:] = scaling.fit_transform(df[:])
        
        logging.info("scale data")
        return df

    def normalizer(self, df):
        scaler = StandardScaler()
        scaled = pd.DataFrame(scaler.fit_transform(df))
        logging.info("normalize data")

        return scaled

    def target_feature(self, df, f_r, t):
        
        features = (df.drop(df.columns[[t]], axis = 1)).values
        target = df.iloc[:,t].values
        return features, target

    def set_splitter(self, input, test, val, rand_state):
        features, target = input
        per_1 = test
        per_2 = (1-test)*val
        x_train, x_test, y_train, y_test = train_test_split(features, target,test_size= per_1,shuffle = True, random_state = rand_state )
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,test_size= per_2, shuffle = True, random_state = rand_state)

        logging.info("data splitter")


        return [x_train, y_train, x_test, y_test, x_val, y_val]
