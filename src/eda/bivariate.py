import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def bivariate_analysis(df: pd.DataFrame, output_dir: str):
    """Perform bivariate analysis."""
    os.makedirs(output_dir, exist_ok=True)
    logger.info("Starting bivariate analysis")
    
    # Scatter plot: TotalPremium vs TotalClaims
    plt.figure(figsize=(10, 6))
    sns.scatterplot(x='TotalPremium', y='TotalClaims', hue='Province', data=df)
    plt.title("TotalPremium vs TotalClaims by Province")
    plt.savefig(os.path.join(output_dir, "premium_vs_claims_province.png"))
    plt.close()
    
    # Correlation matrix
    numerical_cols = ['TotalPremium', 'TotalClaims', 'SumInsured']
    corr = df[numerical_cols].corr()
    plt.figure(figsize=(8, 6))
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.title("Correlation Matrix")
    plt.savefig(os.path.join(output_dir, "correlation_matrix.png"))
    plt.close()
    