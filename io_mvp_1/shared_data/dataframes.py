# shared/dataframe.py

# ------------------- GLOBAL STORE -------------------
# This dict will hold different stages of DataFrames
data_store = {
    "input": {},        # Raw uploaded/sample data
    "cleaned": {},      # After cleaning
    "aggregated": {},   # After aggregation
    "distributed": {},  # After distribution
    "schedule": {},     # After scheduling
}

# ------------------- API -------------------
def set_stage(stage: str, dfs: dict):
    """
    Save a dictionary of DataFrames for a given stage.
    
    Args:
        stage (str): One of ["input", "cleaned", "aggregated", "distributed", "schedule"]
        dfs (dict): {key: DataFrame}
    """
    if stage not in data_store:
        raise ValueError(f"Invalid stage: {stage}")
    data_store[stage] = dfs


def get_stage(stage: str) -> dict:
    """
    Get all DataFrames for a stage.
    
    Returns:
        dict of {key: DataFrame}
    """
    return data_store.get(stage, {})


def get_dataframe(stage: str, key: str):
    """
    Get a single DataFrame by stage and key.
    
    Example:
        get_dataframe("input", "Orders")
    """
    return data_store.get(stage, {}).get(key)
