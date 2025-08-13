import sqlalchemy
import pandas as pd
from dotenv import load_dotenv
import os

def load_dataframe(table_name: str, column_names: list[str], data: pd.DataFrame):
    load_dotenv()

    host_name = os.environ.get("POSTGRES_HOST")
    database_name = os.environ.get("POSTGRES_DB")
    user_name = os.environ.get("POSTGRES_USER")
    user_password = os.environ.get("POSTGRES_PASSWORD")

    conn_string = f'postgresql+psycopg://{user_name}:{user_password}@{host_name}:5432/{database_name}'
    engine = sqlalchemy.create_engine(conn_string)

    data.columns = column_names

    try:
        data.to_sql(
            table_name,
            con=engine,
            if_exists='append',
            index=False
        )
        print(f"{len(data)} rows have been successfully uploaded to {table_name}.")
    except Exception as e:
        print(f"Error uploading data: {e}")
