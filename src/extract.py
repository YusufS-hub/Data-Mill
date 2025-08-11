import pandas as pd


def extract_data(csv_file):
    try:
        df = pd.read_csv(csv_file)
    except (FileExistsError,FileNotFoundError) as e:
        print('Error extracting data: ', e)
        return None
    
    return df
