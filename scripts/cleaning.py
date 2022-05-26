import pandas as pd
import numpy as np
from regex import D
from vizualisation import Data_Viz
import logging
from logging.handlers import TimedRotatingFileHandler

#class responsible for data cleaning
class DataCleaner:

    logging.basicConfig(filename="../logs/clean.log", level=logging.INFO, format="time: %(asctime)s, function: %(funcName)s, module: %(name)s, message: %(message)s \n")
    def __init__(self) -> None:
        self.summar = Data_Viz() 
        
    def rename(self, df:pd.DataFrame, col:str, old:str, new:str):
        df[col] = df[col].replace([old], new)
        logging.info("function to rename columns")
        return(df[col].value_counts().index)

    def replace_rows_str(self, df:pd.DataFrame, col:str):
        df[col] = df[col].map(str)
        df[col] = df[col].apply(str)
        df[col] = df[col].astype(str)
        df[col] = df[col].values.astype(str)
        logging.info("function to change to string")
        return(df[col].value_counts().index)
    
    def fill_outliers_mean(self, df, cols):
        df_temp = df.copy(deep=True)
        for col in cols:
            Q1 = df_temp[col].quantile(0.25)

            Q3 = df_temp[col].quantile(0.75)
            IQR = Q3 - Q1

            length=df_temp.shape[0]
            for index in range(length):
                if(df_temp.loc[index,col] >= (Q3+1.5*IQR)):
                    df_temp.loc[index,col] = np.nan

            df_temp = self.fill_missing_by_median(df_temp, cols)
        logging.info("fill outliers with mean")
        return df_temp


    def removeOutliers(self, df,cols):
        df_temp = df.copy(deep=True)
        for col in cols:
            Q1 = df_temp[col].quantile(0.25)

            Q3 = df_temp[col].quantile(0.75)
            IQR = Q3 - Q1
            rm_lis = []
            length=df_temp.shape[0]
            for index in range(length):
                if(df_temp.loc[index,col] >= (Q3+1.5*IQR)):
                    rm_lis.append(index)

            df_temp.drop(rm_lis, inplace = True)
            logging.info("remove outliers")

        return df_temp
    
    def remove_cols(self, df, cols, keep=False):
        if(keep):
            r_df = df.loc[:,cols]
        else:
            r_df = df.drop(cols, axis=1)

        logging.info("drop columns")
        return r_df

    def reduce_dim_missing(self, df,limit):
        
        temp = self.summar.summ_columns(df)
        rem_lis = []
        for i in range(temp.shape[0]):
            if(temp.iloc[i,2] > limit):
                rem_lis.append(temp.iloc[i,0])
        r_df = df.drop(rem_lis, axis=1) 
        
        return r_df

    
    def fill_missing_by_mode(self, df, cols=None):
        
        mod_fill_list = []
        if(cols == None):
            temp = self.summar.summ_columns(df)
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "object"):
                    mod_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                mod_fill_list.append(col)
        
        for col in mod_fill_list:
            df[col] = df[col].fillna(df[col].mode()[0])
        logging.info("fill missing by mode")        
        return df


    def fill_missing_by_mean(self, df, cols=None):
        
        temp = self.summar.summ_columns(df)
        mean_fill_list = []
        
        if cols is None:
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "float64"):
                    mean_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                mean_fill_list.append(col)
        
        for col in mean_fill_list:
            df[col] = df[col].fillna(df[col].median())
        
        logging.info("fill missing by mean")
        return df

    def fill_missing_by_median(self, df, cols=None):
       
        temp = self.summar.summ_columns(df)
        median_fill_list = []

        if cols is None:
            for i in range(temp.shape[0]):
                if(temp.iloc[i,3] == "float64" or temp.iloc[i,3] == "int64"):
                    median_fill_list.append(temp.iloc[i,0])
        else:
            for col in cols:
                median_fill_list.append(col)

        for col in median_fill_list:
            df[col] = df[col].fillna(df[col].median())

        logging.info("fill missing by median")
        return df


    def fill_missing_forward(self, df, cols):
        
        for col in cols:
            df[col] = df[col].fillna(method='ffill')

        return df

    def fill_missing_backward(self, df, cols):
        
        for col in cols:
            df[col] = df[col].fillna(method='bfill')
        return df


    


    

    

    
