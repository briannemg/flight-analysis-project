import pandas as pd

def load_flight_data(file_path: str) -> pd.DataFrame:
    """Load flight CSV data and return a DataFrame."""
    return pd.read_csv(file_path)