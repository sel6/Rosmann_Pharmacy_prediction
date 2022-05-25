import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import FunctionTransformer

class DataTransformer:
    """
    provides transformer functions for machine learning.
    """
    def __init__(self) -> None:
        pass


    def sep_cat_num(self, df):
        """
        separates categorical and numerical variables
        """
        categorical_columns = df.select_dtypes(include='object')
        numerical_columns = df.select_dtypes(exclude='object')

        return categorical_columns, numerical_columns

    
    def cat_labeler(self, df, cat_cols):
        """
        assigns a numerical label to categorical values
        """
        for column in cat_cols:
            encoder = LabelEncoder()
            df[column] = encoder.fit_transform(df[column])
        
        print("catagories successfully labeled")

        return df


    def scaler(self, df):
        """
        transforms values within 0 to 1 range
        """
        scaling = MinMaxScaler()
        df[:] = scaling.fit_transform(df[:])

        print("Data successfully scaled")
        
        return df

    def normalizer(self, df):
        """
        normalizing. turning mean to 0 and SD to 1
        """
        # define standard scaler
        scaler = StandardScaler()
        # transform data
        scaled = pd.DataFrame(scaler.fit_transform(df))

        print("Data successfully normalized")

        return scaled

    def target_feature(self, df, f_r, t):
        """
        target and feature separator
        """
        features = df.iloc[:,f_r[0]:f_r[1]].values
        target = df.iloc[:,t].values
        
        print("target and features separated")

        return features, target

    def set_splitter(self, input, test, val, rand_state):
        """
        splits dataset into specified percentages.
        """
        features, target = input
        per_1 = test
        per_2 = (1-test)*val
        x_train, x_test, y_train, y_test = train_test_split(features, target,test_size= per_1,shuffle = True, random_state = rand_state )
        x_train, x_val, y_train, y_val = train_test_split(x_train, y_train,test_size= per_2, shuffle = True, random_state = rand_state)

        print("data successfully splitted")


        return [x_train, y_train, x_test, y_test, x_val, y_val]