from src.data.load_data import load_raw_data
from src.data.clean_data import clean_data
from src.stats.hypothesis_tests import hypothesis_tests
import logging
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def run_stats():
    """Run statistical analysis pipeline."""
    config_path = "config.yaml"
    df = load_raw_data(config_path)
    df_clean = clean_data(df, config_path)
    logger.info(f"DataFrame columns: {df_clean.columns.tolist()}")
    results = hypothesis_tests(df_clean, config_path)
    print(results)

if __name__ == "__main__":
    run_stats()