import pandas as pd
import scipy.stats as stats
import logging
import yaml
from src.utils.logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


def hypothesis_tests(df: pd.DataFrame, config_path: str):
    """Perform hypothesis tests for risk and margin differences."""
    with open(config_path, 'r') as file:
        yaml.safe_load(file)  # config loaded but not used # for future use
    logger.info("Starting hypothesis tests")

    results = []

    # Define metrics
    df['HasClaim'] = df['TotalClaims'] > 0
    df['ClaimSeverity'] = df['TotalClaims'].where(df['HasClaim'], None)
    df['Margin'] = df['TotalPremium'] - df['TotalClaims']

    # H0: No risk differences across provinces
    provinces = df['Province'].unique()
    logger.info(f"Testing provinces: {provinces}")
    chi2, pval = stats.chi2_contingency(
        pd.crosstab(df['Province'], df['HasClaim'])
    )[:2]
    results.append({
        'Hypothesis': 'No risk differences across provinces',
        'Metric': 'Claim Frequency',
        'p-value': pval,
        'Result': 'Reject' if pval < 0.05 else 'Fail to Reject'
    })

    # H0: No risk differences between zip codes
    zip_codes = df['PostalCode'].value_counts().head(10).index
    logger.info(f"Testing zip codes: {zip_codes}")
    chi2, pval = stats.chi2_contingency(
        pd.crosstab(
            df[df['PostalCode'].isin(zip_codes)]['PostalCode'],
            df['HasClaim']
        )
    )[:2]
    results.append({
        'Hypothesis': 'No risk differences between zip codes',
        'Metric': 'Claim Frequency',
        'p-value': pval,
        'Result': 'Reject' if pval < 0.05 else 'Fail to Reject'
    })

    # H0: No significant margin difference between zip codes
    margins = [df[df['PostalCode'] == z]['Margin'].dropna() for z in zip_codes]
    f_stat, pval = stats.f_oneway(*margins)
    results.append({
        'Hypothesis': 'No significant margin difference between zip codes',
        'Metric': 'Margin',
        'p-value': pval,
        'Result': 'Reject' if pval < 0.05 else 'Fail to Reject'
    })

    # H0: No significant risk difference between Women and Men
    genders = ['Male', 'Female']
    logger.info(f"Testing genders: {genders}")
    chi2, pval = stats.chi2_contingency(
        pd.crosstab(
            df[df['Gender'].isin(genders)]['Gender'],
            df['HasClaim']
        )
    )[:2]
    results.append({
        'Hypothesis': 'No significant risk difference between genders',
        'Metric': 'Claim Frequency',
        'p-value': pval,
        'Result': 'Reject' if pval < 0.05 else 'Fail to Reject'
    })

    # Save results
    results_df = pd.DataFrame(results)
    results_df.to_csv('reports/hypothesis_test_results.csv', index=False)
    logger.info(
        "Hypothesis test results saved to reports/hypothesis_test_results.csv"
    )

    return results_df
