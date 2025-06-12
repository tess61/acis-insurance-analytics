# ACIS Insurance Analytics

This repository contains the data analytics pipeline for AlphaCare Insurance Solutions (ACIS) to optimize car insurance marketing and pricing strategies in South Africa. The project includes exploratory data analysis (EDA), statistical hypothesis testing, machine learning modeling, and data version control using DVC.

## Project Structure
    acis-insurance-analytics/
├── data/
│   ├── raw/                    # Raw data (e.g., MachineLearningRating_v3.txt)
│   ├── processed/              # Cleaned and processed data
│   └── external/               # External data sources (if any)
├── src/
│   ├── data/                   # Data processing scripts
│   │   ├── __init__.py
│   │   ├── load_data.py
│   │   ├── clean_data.py
│   │   └── preprocess.py
│   ├── eda/                    # Exploratory Data Analysis scripts
│   │   ├── __init__.py
│   │   ├── univariate.py
│   │   ├── bivariate.py
│   │   └── visualizations.py
│   ├── stats/                  # Statistical testing scripts
│   │   ├── __init__.py
│   │   └── hypothesis_tests.py
│   ├── modeling/               # Machine learning models
│   │   ├── __init__.py
│   │   ├── linear_regression.py
│   │   ├── random_forest.py
│   │   ├── xgboost_model.py
│   │   └── evaluation.py
│   └── utils/                  # Utility functions
│       ├── __init__.py
│       ├── logging_config.py
│       └── helpers.py
├── tests/                      # Unit tests
│   ├── __init__.py
│   ├── test_data.py
│   └── test_models.py
├── notebooks/                  # Jupyter notebooks for experimentation
│   └── eda_exploration.ipynb
├── reports/                    # Reports and visualizations
│   ├── figures/                # Plots and charts
│   └── final_report.md
├── .github/
│   └── workflows/
│       └── ci.yml              # GitHub Actions CI/CD pipeline
├── dvc/                        # DVC storage (local)
├── .gitignore
├── README.md
├── requirements.txt
├── setup.py
├── dvc.yaml
└── config.yaml                 # Configuration file for parameters

## Setup
1. Clone the repository:
     bash```
         `git clone https://github.com/tess61/acis-insurance-analytics.git`
        ```
2. Create a virtual environment:  
    bash ``` 
        `python -m venv venv` 
    ```
3. Activate the environment: 
    bash``` 
        `source venv/bin/activate` 
    ```
4. Install dependencies: 
    bash ``` 
        `pip install -r requirements.txt` 
    ```
5. Initialize DVC:
    bash ``` 
        `dvc init`  
    ```

## Usage
- Run EDA: `python src/eda/main.py`
- Run statistical tests: `python src/stats/hypothesis_tests.py`
- Train models: `python src/modeling/main.py`

## License
Proprietary - AlphaCare Insurance Solutions