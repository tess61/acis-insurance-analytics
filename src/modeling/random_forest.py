from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
import logging
from src.utils.logging_config import setup_logging


setup_logging()
logger = logging.getLogger(__name__)


def train_random_forest(X_train, X_test, y_train, y_test):
    """Train and evaluate a Random Forest model."""
    logger.info("Training Random Forest model")
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    # Predictions
    y_pred = model.predict(X_test)
    
    # Evaluation
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)
    
    logger.info(f"Random Forest - RMSE: {rmse:.2f}, R2: {r2:.2f}")
    return model, {'RMSE': rmse, 'R2': r2}
