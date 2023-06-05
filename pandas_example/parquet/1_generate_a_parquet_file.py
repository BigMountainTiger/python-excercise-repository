
import pandas as pd
import numpy as np


def run():

    technologies = {
        'Courses': ["Spark No.1", "PySpark No.1", "Spark NO.2", "Python", "PySpark No.2"],
        'Fee': [22000, 25000, 23000, 24000, 26000],
        'Duration': ['30days', '50days', '30days', None, np.nan]
    }

    df = pd.DataFrame(technologies)
    print(df)

    file_name = 'example.parquet'
    df.to_parquet(f'parquet-files/{file_name}')


if __name__ == '__main__':
    run()
