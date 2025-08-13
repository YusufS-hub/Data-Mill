import extract as e
import transform as t
import load as l
import path
import os

# List of all csv files to be loaded into the DB
csv_files = ['anime_messy.csv']

for file in csv_files:
    # Specify file path
    csv_file = os.path.join(path.data_dir, file)

    # Step 1: Extract data from CSV file using pandas
    raw_data = e.extract_data(csv_file)

    # Step 2: Transform data to normal form
    # Replace 'transfomed_anime' with the correct transformation function
    clean_anime_data = t.transformed_anime(raw_data)

    # Step 3: Load data into DB
    l.load_dataframe(
        'clean_anime',
        ['anime_id', 'anime_name', 'genre_name', 'anime_type', 'episodes_number', 'rating', 'members'],
        clean_anime_data
    )
