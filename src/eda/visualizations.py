import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import logging
import os
from src.utils.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def create_insight_plots(df: pd.DataFrame, output_dir: str):
    """Create three insightful visualizations."""
    os.makedirs(output_dir, exist_ok=True)
    logger.info("Creating insight plots")
    
    # Plot 1: Loss Ratio by Province
    df['LossRatio'] = df['TotalClaims'] / df['TotalPremium'].replace(0, 1)
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Province', y='LossRatio', data=df)
    plt.title("Loss Ratio by Province")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, "loss_ratio_province.png"))
    plt.close()
    
    # Plot 2: Claim Frequency by Vehicle Type
    df['HasClaim'] = df['TotalClaims'] > 0
    claim_freq = df.groupby('VehicleType')['HasClaim'].mean().reset_index()
    plt.figure(figsize=(12, 6))
    sns.barplot(x='VehicleType', y='HasClaim', data=claim_freq)
    plt.title("Claim Frequency by Vehicle Type")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, "claim_freq_vehicle_type.png"))
    plt.close()
    
    # Plot 3: Temporal Trend of Claims
    df['TransactionMonth'] = pd.to_datetime(df['TransactionMonth'], errors='coerce')
    monthly_claims = df.groupby(df['TransactionMonth'].dt.to_period('M'))['TotalClaims'].sum().reset_index()
    # Convert Period to string for plotting
    monthly_claims['TransactionMonth'] = monthly_claims['TransactionMonth'].astype(str)
    # Debug: Inspect the DataFrame
    logger.info("Inspecting monthly_claims DataFrame:")
    logger.info(f"monthly_claims head:\n{monthly_claims.head()}")
    logger.info(f"monthly_claims dtypes:\n{monthly_claims.dtypes}")
    # Ensure TotalClaims is numeric
    monthly_claims['TotalClaims'] = pd.to_numeric(monthly_claims['TotalClaims'], errors='coerce')
    if monthly_claims['TotalClaims'].isna().sum() > 0:
        logger.warning(f"Found {monthly_claims['TotalClaims'].isna().sum()} NaN values in TotalClaims; dropping them")
        monthly_claims = monthly_claims.dropna(subset=['TotalClaims'])
    
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='TransactionMonth', y='TotalClaims', data=monthly_claims)
    plt.title("Monthly Total Claims Trend")
    plt.xticks(rotation=45)
    plt.savefig(os.path.join(output_dir, "claims_trend.png"))
    plt.close()