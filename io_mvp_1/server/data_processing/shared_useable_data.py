import os
import pandas as pd
from shared_data import dataframe   # import your new global store

# ------------------- GLOBAL STORE -------------------
dataframes = {}

# ------------------- HELPERS -------------------
def _read_file(path):
    """Read CSV or Excel into DataFrame."""
    if path.endswith(".csv"):
        return pd.read_csv(path)
    elif path.endswith((".xls", ".xlsx")):
        return pd.read_excel(path)
    else:
        raise ValueError(f"Unsupported file format: {path}")


def load_uploaded_files(uploaded_files, save_paths):
    """
    Convert uploaded files into DataFrames and save copies in SHARED_DIR.
    
    Args:
        uploaded_files (dict): {key: file_object} from st.file_uploader
        save_paths (dict): {key: save_path} where each file should be stored

    Returns:
        dict of {key: DataFrame}
    """
    global dataframes
    dataframes = {}

    for key, file_obj in uploaded_files.items():
        try:
            # Save uploaded file to shared path
            save_path = save_paths[key]
            with open(save_path, "wb") as f:
                f.write(file_obj.getbuffer())

            # Load into DataFrame
            df = _read_file(save_path)
            dataframes[key] = df
        except Exception as e:
            print(f"[ERROR] {key}: {e}")

    return dataframes


def load_sample_files() -> dict:
    """
    Load sample data from the predefined 'server/data' folder.

    Returns:
        dict: {key: DataFrame}
    """
    global dataframes
    dataframes = {}

    # Path to your static data folder
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_folder = os.path.join(base_dir, "..", "..", "server", "data")

    # Map logical names to actual CSV filenames
    file_map = {
        "Orders": "orders.csv",
        "Inventory": "inventory.csv",
        "Demand Forecast": "demand_forecast.csv",
        "Lead Time": "lead_time.csv",
        "Node Data": "node_data.csv",
    }

    for key, filename in file_map.items():
        path = os.path.join(data_folder, filename)
        try:
            df = _read_file(path)
            dataframes[key] = df
        except Exception as e:
            print(f"[ERROR] {key}: {e}")

    # Save into central store as "input"
    dataframe.set_stage("input", dataframes)

    return dataframes

def get_data(key):
    """
    Retrieve a specific dataframe.
    """
    return dataframes.get(key)


