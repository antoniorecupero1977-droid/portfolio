# Climate Change Analysis & Forecast

This project analyzes historical global temperature anomalies using NASA GISTEMP data and provides predictions for the next 50 years using two different models.

## Data Source
- NASA Goddard Institute for Space Studies (GISS) Surface Temperature Analysis (GISTEMP):  
  [https://data.giss.nasa.gov/gistemp/](https://data.giss.nasa.gov/gistemp/)

## Features
- Download and clean historical temperature anomaly data (1880 - present)
- Perform and compare:
  - **Linear regression prediction**
  - **Polynomial regression prediction** (degree 3)
- Visualize historical data along with both forecasts on a single plot

## Files
- `climate_prediction.py` → Python script version (standalone execution)
- `climate_prediction.ipynb` → Jupyter Notebook version, including explanatory comments and step-by-step execution

## Requirements
Install dependencies with:
```bash
pip install pandas numpy matplotlib scikit-learn requests
```

## How to Run
### Python Script
```bash
python climate_prediction.py
```

### Jupyter Notebook
Open in JupyterLab or Jupyter Notebook:
```bash
jupyter notebook climate_prediction.ipynb
```

The script will:
1. Download the latest NASA GISTEMP dataset
2. Clean and process the data
3. Generate predictions up to the year 2075
4. Save a plot (`climate_prediction_plot.png`) showing historical and predicted trends
