import pandas as pd

def test_rownum():
    df=pd.read_csv("input.txt",encoding='utf-16be',escapechar='\\',na_values='--',index_col=0)
    assert len(df.columns)==31
    assert len(df.index)==225



