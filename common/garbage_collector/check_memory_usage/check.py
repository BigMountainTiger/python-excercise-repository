import psutil
import numpy as np
import pandas as pd


process = psutil.Process()


def get_current_memory_usage():
    memory_mb = process.memory_info().rss / (1024 * 1024)
    return f"{memory_mb} M"


def get_a_pandas_dataframe_generator(no_of_dataframes):

    def create_a_large_dataframe():
        n_rows = 1_000_000
        df = pd.DataFrame(
            {
                "id": np.arange(n_rows),
                "value": np.random.randn(n_rows),
                "category": np.random.choice(["A", "B", "C"], size=n_rows),
                "timestamp": pd.date_range("2025-01-01", periods=n_rows, freq="s"),
            }
        )

        return df

    while no_of_dataframes > 0:
        yield create_a_large_dataframe()
        no_of_dataframes -= 1


print(f"Memory usage begin at {get_current_memory_usage()}")

dfs = get_a_pandas_dataframe_generator(5)
print()

i = 0
columns = None
for df in dfs:
    i += 1
    print(f"Memory usage when receive No.{i} dataframe: {get_current_memory_usage()}")

    # Hold a referece to the column strings do not block gargabe collection
    columns = [c for c in df.columns] if columns is None else columns

    del df
    print(f"Memory usage IMMEDIATELY after de-referencing No.{i} dataframe: {get_current_memory_usage()}")
    print()

print(columns)
