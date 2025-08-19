import pandas as pd


def extract_data(csv_file):
    try:
        df = pd.read_csv(csv_file, names = ['anime_id','name','genre','type','episodes','rating','members'])
    except (FileExistsError,FileNotFoundError) as e:
        print('Error extracting data: ', e)
        return None
    
    return df
