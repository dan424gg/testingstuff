import os
from sqlalchemy import create_engine
import pandas as pd

conn_url = os.getenv('DATABASE_URL', None)
engine = create_engine(conn_url)

with engine.connect() as conn:
    df = pd.DataFrame([1,2,3], columns=['test_col'])
    df.to_sql('dealer', conn)

    df = pd.read_sql_table('dealer', conn)
    print(df)