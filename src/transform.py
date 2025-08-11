import pandas as pd
import extract as e
from path import csv_file

path = csv_file
df = e.extract_data(path)

def clean_products(df:pd.DataFrame):
    try:
        df = df.copy()
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        clean_df = df
    except Exception as e:
        print('Error cleaning data: ', e)
        return None
    return clean_df

def transform_release_date():
    try:
        df['ReleaseDate'] = pd.to_datetime(df['ReleaseDate'], errors='coerce', dayfirst=False)
        df['ReleaseDate'] = df['ReleaseDate'].dt.strftime('%m-%d-%Y')
    except Exception as e:
        print('Error transforming release date: ', e)
        return None
    return df

def transform_rating(rating):
    try:
        if pd.isna(rating):
            return None
        rating = str(rating).strip()
        
        if '%' in rating:
            

        
    

df = clean_products(df)
print(df)
