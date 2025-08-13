import pandas as pd

def clean_data(df: pd.DataFrame):
    if df is None:
        return None
    try:
        df = df.copy()
        df.dropna(inplace=True)
        df.drop_duplicates(inplace=True)
        return df
    except Exception as e:
        print('Error cleaning data: ', e)
        return None

def clean_names(df: pd.DataFrame):
    if df is None or 'name' not in df.columns:
        return df
    df = df.copy()
    df['name'] = df['name'].astype(str).str.strip().str.replace(r'[0-9°\$£#!:;$%^&*().<>]', '', regex=True)
    return df

def clean_genre(df: pd.DataFrame):
    if df is None or 'genre' not in df.columns:
        return df
    df = df.copy()
    df['genre'] = df['genre'].astype(str).str.strip().str.replace(r'[,]', ' - ', regex=True)
    return df

def clean_episodes(df: pd.DataFrame):
    if df is None or 'episodes' not in df.columns:
        return df
    df = df.copy()
    df['episodes'] = df['episodes'].astype(str).str.strip().str.replace(r'[eps]', '', regex=True)
    df = df.fillna(value=pd.NA)
    return df

def clean_rating(df: pd.DataFrame):
    if df is None or 'rating' not in df.columns:
        return df
    df = df.copy()
    df['rating'] = df['rating'].astype(str).str.strip().str.replace(r'[/10]', '', regex=True)
    df = df.fillna(value=pd.NA)
    df['rating'] = pd.to_numeric(df['rating'].astype(str).str.replace('/10', '', regex=False), errors='coerce')
    return df

def clean_members(df: pd.DataFrame):
    if df is None or 'members' not in df.columns:
        return df
    df = df.copy()
    df['members'] = df['members'].astype(str).str.lstrip().str.replace(r'[members]', '', regex=True)
    return df

def clean_type(df: pd.DataFrame):
    if df is None or 'type' not in df.columns:
        return df
    df = df.copy()
    df['type'] = df['type'].astype(str).str.strip().str.replace(r'[,]', ' - ', regex=True)
    return df


def transformed_anime(df: pd.DataFrame):
    df = clean_data(df)
    df = clean_names(df)
    df = clean_genre(df)
    df = clean_episodes(df)
    df = clean_rating(df)
    df = clean_type(df)
    df = clean_members(df)
    return df

def run_transform(csv_path):
    import extract as e
    df = e.extract_data(csv_path)
    df = transformed_anime(df)
    print(df)
    return df


    
