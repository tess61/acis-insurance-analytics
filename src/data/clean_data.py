import pandas as pd
import logging
import yaml
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame, config_path: str) -> pd.DataFrame:
    """Clean the raw dataset."""
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)
    logger.info("Starting data cleaning")

    # Handle missing values
    df = df.fillna(
        {
            "Gender": "Unknown",
            "MaritalStatus": "Unknown",
            "PostalCode": "Unknown",
            "TotalPremium": 0,
            "TotalClaims": 0,
            "TransactionMonth": pd.NaT,
        }
    )

    # Convert TransactionMonth to datetime
    df["TransactionMonth"] = pd.to_datetime(
        df["TransactionMonth"], errors="coerce"
    )
    invalid_dates = df["TransactionMonth"].isna().sum()
    if invalid_dates > 0:
        msg = f"Found {invalid_dates} invalid TransactionMonth values; dropping them"
        logger.warning(msg)
        df = df.dropna(subset=["TransactionMonth"])

    # Ensure numerical columns are numeric
    for col in ["TotalPremium", "TotalClaims"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")
        invalid_values = df[col].isna().sum()
        if invalid_values > 0:
            logger.warning(f"Found {invalid_values} invalid {col} values; filling with 0")
            df[col] = df[col].fillna(0)

    # Log summary statistics
    logger.info("Summary statistics after cleaning:")
    logger.info(f"Total rows: {len(df)}")
    logger.info(f"TransactionMonth dtype: {df['TransactionMonth'].dtype}")
    logger.info(f"TotalClaims dtype: {df['TotalClaims'].dtype}")

    # Save cleaned data
    output_path = config["data"]["processed_path"]
    df.to_csv(output_path, index=False)
    logger.info(f"Cleaned data saved to {output_path}")
    return df