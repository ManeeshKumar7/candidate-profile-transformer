from pathlib import Path

import pandas as pd


class CSVReader:
    """
    Reads recruiter CSV.
    """

    def read(self, file_path: str | Path) -> pd.DataFrame:

        dataframe = pd.read_csv(file_path)

        dataframe.columns = dataframe.columns.str.strip()

        return dataframe