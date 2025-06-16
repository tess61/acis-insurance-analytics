from src.data.load_data import load_raw_data
from src.data.clean_data import clean_data
from src.data.preprocessing import preprocess_data
from src.modeling.linear_regression import train_linear_regression
from src.modeling.random_forest import train_random_forest
from src.modeling.xgboost_model import train_xgboost
from src.modeling.evaluation import evaluate_models
import yaml


def run_modeling():
    """Run the modeling pipeline."""
    config_path = "config.yaml"
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    # Load and preprocess data
    df = load_raw_data(config_path)
    df_clean = clean_data(df, config_path)
    X_train, X_test, y_train, y_test = preprocess_data(df_clean, config_path)

    # Train models
    models = {}
    models['Linear Regression'] = train_linear_regression(
        X_train, X_test, y_train, y_test
        )
    models['Random Forest'] = train_random_forest(
        X_train, X_test, y_train, y_test
        )
    models['XGBoost'] = train_xgboost(
        X_train, X_test, y_train, y_test
        )

    # Evaluate models
    output_dir = config['eda']['output_dir']
    results = evaluate_models(models, X_test, output_dir)
    print(results)


if __name__ == "__main__":
    run_modeling()
