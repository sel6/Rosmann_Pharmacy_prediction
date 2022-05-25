import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

class Data_Viz:
    
    def barplot(self, df:pd.DataFrame, cols, x:str):
        plot_df = df[cols]
        plt.figure(figsize=(10, 10))
        sns.countplot(x=x, data=plot_df)
    
    def two_barplot(self, df:pd.DataFrame, df2:pd.DataFrame, t1:str, t2:str, t3:str, t4:str, t5:str, t6:str):
        fig, (axis1,axis2) = plt.subplots(1,2,figsize=(12,4))
        sns.barplot(x=t1, y=t2, data=df, ax=axis1).set_title(t3)
    
        sns.barplot(x=t4, y=t5, data=df2, ax=axis2).set_title(t6)
        plt.show()
        
    def plot_counts2(self, df:pd.DataFrame, column:str, second_column=None):
        cols = ['blue','red']
        labels = ['With','Without']
        for i in reversed(range(0,2)):
            promos = df[df[column] == i][second_column]
            plt.hist(promos, 
            color=cols[i], alpha=0.3, label =labels[i])

        plt.ylabel(column)
        plt.xlabel(second_column)
        plt.legend()
        plt.plot()
    
    def plot_counts(self, df:pd.DataFrame, column:str, second_column=None):
        sns.countplot( x=column, data=df, hue=second_column)
        plt.show()
    
    
    def heat_map(self, df:pd.DataFrame):
        plt.figure(figsize=(10,9))
        sns.heatmap(df.corr(), linewidths=0.1, vmax=1.0, 
            square=True, cmap=plt.cm.RdBu, linecolor='white', annot=True)
    
    def binom_distribution(self, C_aware, C_total, C_cr, E_cr) -> None:
        fig, ax = plt.subplots(figsize=(12,6))
        x = np.linspace(C_aware-49, C_aware+50, 100)
        y = scs.binom(C_total, C_cr).pmf(x)
        ax.bar(x, y, alpha=0.5)
        ax.axvline(x=E_cr * C_total, c='blue', alpha=0.75, linestyle='--')
        plt.xlabel('Aware')
        plt.ylabel('probability')
        plt.show()

    def plot_box(self, df:pd.DataFrame, columns, color:str)->None:
        fig = plt.figure(figsize =(10, 7))
        
        for col in columns:
            # Creating plot
            plt.boxplot(df[columns])
            plt.title(f'Plot of {col}', size=20, fontweight='bold')
            ax = plt.gca()
            ax.set_ylim(top = df[col].quantile(0.9999))
            ax.set_ylim(bottom = 0)
            # show plot
            plt.show()

    def plot_box2(self, df:pd.DataFrame, col:str)->None:
        """
        Boxplot plotting function.
        """
        plt.boxplot(df[col])
        plt.title(f'Plot of {col}', size=20, fontweight='bold')
        ax = plt.gca()
        #ax.set_ylim(top = df[col].quantile(0.9999))
        #ax.set_ylim(bottom = 0)
        # show plot
        plt.show()


    def plot_pie(self, df, col, title):
        wp = { 'linewidth' : 1, 'edgecolor' : "black" }
        def func(pct, allvalues):
            absolute = int(pct / 100.*np.sum(allvalues))
            return "{:.1f}%\n({:d} g)".format(pct, absolute)
        
        fig, ax = plt.subplots(figsize =(10, 7))
        wedges, texts, autotexts = ax.pie(df[col[1]],
                                    autopct = lambda pct: func(pct, df[col[1]]),
                                    labels = df[col[0]].to_list(),
                                    startangle = 90,
                                    wedgeprops = wp,)

        plt.setp(autotexts, size = 8, weight ="bold")
        ax.set_title(title)


    def show_distribution(self, df, col, color, title):
        sns.displot(data=df, x=col, color=color, kde=True, height=4, aspect=2)
        plt.title(title, size=15, fontweight='bold')
        plt.show()
            

    def summ_columns(self, df, unique=True):
        
        df2 = df.isna().sum().to_frame().reset_index()
        df2.rename(columns = {'index':'variables', 0:'missing_count'}, inplace = True)
        df2['missing_percent_(%)'] = round(df2['missing_count']*100/df.shape[0])
        data_type_lis = df.dtypes.to_frame().reset_index()
        df2['data_type'] = data_type_lis.iloc[:,1]
        
        if(unique):
            unique_val = []
            for i in range(df2.shape[0]):
                unique_val.append(len(pd.unique(df[df2.iloc[i,0]])))
            df2['unique_values'] = pd.Series(unique_val)
        return df2

    
    def percent_missing(df: pd.DataFrame):

        # Calculate total number of cells in dataframe
        totalCells = np.product(df.shape)

        # Count number of missing values per column
        missingCount = df.isnull().sum()

        # Calculate total number of missing values
        totalMissing = missingCount.sum()

        # Calculate percentage of missing values
        print("The dataset contains", round(
            ((totalMissing/totalCells) * 100), 2), "%", "missing values.")
