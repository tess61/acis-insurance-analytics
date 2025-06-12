import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)


def univariate_analysis(df: pd.DataFrame, output_dir: str):
    """Perform univariate analysis on numerical and categorical columns."""
    os.makedirs(output_dir, exist_ok=True)
    logger.info("Starting univariate analysis")

    # Numerical columns
    numerical_cols = ["TotalPremium", "TotalClaims", "SumInsured"]
    for col in numerical_cols:
        plt.figure(figsize=(10, 6))
        sns.histplot(df[col], bins=50, kde=True)
        plt.title(f"Distribution of {col}")
        plt.xlabel(col)
        plt.ylabel("Frequency")
        plt.savefig(os.path.join(output_dir, f"{col}_hist.png"))
        plt.close()

    # Categorical columns
    categorical_cols = ["Province", "Gender", "VehicleType"]
    for col in categorical_cols:
        plt.figure(figsize=(10, 6))
        sns.countplot(x=col, data=df)
        plt.title(f"Count of {col}")
        plt.xticks(rotation=45)
        plt.savefig(os.path.join(output_dir, f"{col}_count.png"))
        plt.close()
