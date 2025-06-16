import pandas as pd
import shap
import matplotlib.pyplot as plt
import logging
import os
from src.utils.logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


def evaluate_models(models, X_test, output_dir: str):
    """Evaluate models and analyze feature importance."""
    os.makedirs(output_dir, exist_ok=True)
    logger.info("Evaluating models")
    
    results = []

    for name, (model, metrics) in models.items():
        results.append({'Model': name, **metrics})
        
        
        # SHAP analysis for tree-based models
        if name in ['Random Forest', 'XGBoost']:
            explainer = shap.TreeExplainer(model)
            shap_values = explainer.shap_values(X_test)
            plt.figure()
            shap.summary_plot(shap_values, X_test, show=False)
            plt.savefig(os.path.join(output_dir, f"{name}_shap_summary.png"))
            plt.close()
    
    results_df = pd.DataFrame(results)
    results_df.to_csv(os.path.join(output_dir, "model_comparison.csv"), index=False)
    logger.info("Model comparison saved to model_comparison.csv")
    
    return results_df
