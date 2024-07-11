from typing import Dict

import pandas as pd
from morphdb_utils.annotations import transform
from morphdb_utils.api import ref, send_email  # type: ignore

# The `data` variable prepares the data for processing in the main functions.
# For more information, please read the documentation at https://docs.morphdb.io/dbutils
data: Dict[str, pd.DataFrame] = {}


# The main function runs on the cloud when you click "Run".
# It's used by the data pipeline on the canvas to execute your Directed Acyclic Graph (DAG).
@transform
def main(data: Dict[str, pd.DataFrame]) -> pd.DataFrame:
    # This is where you write your code.

    df = pd.DataFrame(
        {
            "Name": ["John Doe", "Jane Smith", "Emily Zhang"],
            "Age": [28, 34, 22],
            "Occupation": ["Software Engineer", "Data Scientist", "Marketing Manager"],
        }
    )

    print("====================================")
    print('send_email(ref("example_python_cell"), ...)')
    send_email(
        [ref("example_python_cell")],
        ["yuki.ogino@queue-inc.com"],
        "Hello, World!",
        "Hello, World!",
    )

    # print("====================================")
    # print('create_table(df, table_name="test_table")')
    # create_table(df, table_name="test_table")

    return df
