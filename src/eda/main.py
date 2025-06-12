import yaml
from src.data.load_data import load_raw_data
from src.data.clean_data import clean_data
from src.eda.univariate import univariate_analysis
from src.eda.bivariate import bivariate_analysis
from src.eda.visualizations import create_insight_plots


def run_eda():
    """Run the full EDA pipeline."""
    config_path = "config.yaml"
    with open(config_path, "r") as file:
        config = yaml.safe_load(file)

    # Load and clean data
    df = load_raw_data(config_path)
    df_clean = clean_data(df, config_path)

    # Perform EDA
    output_dir = config["eda"]["output_dir"]
    univariate_analysis(df_clean, output_dir)
    bivariate_analysis(df_clean, output_dir)
    create_insight_plots(df_clean, output_dir)


if __name__ == "__main__":
    run_eda()
