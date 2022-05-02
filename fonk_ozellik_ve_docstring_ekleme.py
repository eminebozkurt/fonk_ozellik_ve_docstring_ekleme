#############################################
# Gorev 1
#############################################
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
dataframe = sns.load_dataset("titanic")


def cat_summary(dataframe, col_name, plot=False, desc=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("##########################################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)
    if desc:
        print("################# Describe ###############")
        print(dataframe.describe().T)


cat_summary(dataframe, "survived", False, True)





#############################################
# Gorev 2
#############################################


#check_df

def check_df(dataframe, head=5):
    """
    This function is used for:
    shape: The dimension of dataframe.
    dtypes: It shows type of data.
    head: It shows that the first n rows of dataframe.
    tail: It shows that the first n rows of dataframe.
    isnull: Finds if any NA values in dataframe.
    describe: Analyze of numerical variables.

    Parameters
    ----------
    dataframe : dataframe
        Dataframe is a dataset.
    head : int
        Head shows that the first n rows of a dataframe.

    Returns
    -------

    Examples:
    check_df(df, 4)
    """

    print("############ Shape ###########")
    print(dataframe.shape)
    print("############ Types ###########")
    print(dataframe.dtypes)
    print("############ Head ###########")
    print(dataframe.head(head))
    print("############ Tail ###########")
    print(dataframe.tail(head))
    print("############ NA ###########")
    print(dataframe.isnull().sum())
    print("############ Quantiles ###########")
    print(dataframe.describe([0, 0.05, 0.5, 0.95, 0.99, 1]).T)



check_df(dataframe, head=5)




# cat summary

def cat_summary(dataframe, col_name, plot=False):
    """
    This function gives that the total number according to the variables of the column and ratio.

    Parameters
    ----------
    dataframe : dataframe
        Dataframe is a dataset.
    col_name : str
        The columns of dataframe that is selected.
    plot : bool
        If plot is True, a bar will show the counts of observations.

    Returns
    -------
    Examples:
        cat_summary(dataframe, "sex", plot=False)
    """
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        "Ratio": 100 * dataframe[col_name].value_counts() / len(dataframe)}))
    print("###################")

    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)

cat_summary(dataframe, "sex", plot=True)






