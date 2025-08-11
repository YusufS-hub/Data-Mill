import pandas as pd
import extract as e
from path import csv_file

path = csv_file
df = e.extract_data(path)

print(df)