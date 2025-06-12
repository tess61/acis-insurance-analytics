# ACIS Insurance Analytics

This repository contains the data analytics pipeline for AlphaCare Insurance Solutions (ACIS) to optimize car insurance marketing and pricing strategies in South Africa. The project includes exploratory data analysis (EDA), statistical hypothesis testing, machine learning modeling, and data version control using DVC.

## Project Structure
- `data/`: Raw, processed, and external data.
- `src/`: Python modules for data processing, EDA, statistical tests, and modeling.
- `tests/`: Unit tests for code validation.
- `notebooks/`: Jupyter notebooks for experimentation.
- `reports/`: Final report and visualizations.
- `.github/workflows/`: CI/CD pipeline configuration.

## Setup
1. Clone the repository: `git clone <repo-url>`
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Initialize DVC: `dvc init`

## Usage
- Run EDA: `python src/eda/main.py`
- Run statistical tests: `python src/stats/hypothesis_tests.py`
- Train models: `python src/modeling/main.py`

## License
Proprietary - AlphaCare Insurance Solutions