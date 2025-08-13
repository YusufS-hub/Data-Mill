import pandas as pd
import extract as e
from path import csv_file

path = csv_file
df = e.extract_data(path)

def clean_data(df:pd.DataFrame):
    try:
        df = df.copy()
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        clean_df = df
    except Exception as e:
        print('Error cleaning data: ', e)
        return None
    return clean_df

def clean_names(df: pd.DataFrame):
    cleaned_names = df['name'].str.strip().str.replace(r'[0-9°\$£#!:;$%^&*().<>]', '', regex=True)
    df = df.copy()
    df['name'] = cleaned_names
    return df

def clean_genre(df: pd.DataFrame):
    cleaned_genre = df['genre'].str.strip().str.replace(r'[,]', ' - ', regex=True)
    df = df.copy()
    df['genre'] = cleaned_genre
    return df

def clean_episodes(df: pd.DataFrame):
    cleaned_epi = df['episodes'].str.strip().str.replace(r'[eps]', '', regex=True)
    df = df.copy()
    df['episodes'] = cleaned_epi
    df = df.fillna(value=pd.NA)
    return df

df = clean_names(df)
df = clean_genre(df)
df = clean_episodes(df)

print(df)


    
