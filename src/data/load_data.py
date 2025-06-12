import pandas as pd
import yaml
import logging
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def load_raw_data(config_path: str) -> pd.DataFrame:
    """Load raw data from the specified path in config."""
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    data_path = config['data']['raw_path']
    logger.info(f"Loading data from {data_path}")
    df = pd.read_csv(data_path, sep='|', low_memory=False)
    return df