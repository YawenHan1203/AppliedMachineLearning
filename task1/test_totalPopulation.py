import pandas as pd

def test_totalPopulation():
    df=pd.read_csv("./task1/input.txt",encoding='utf-16be',escapechar='\\',na_values='--',index_col=0)
    assert int(df["2010"].sum())==7065