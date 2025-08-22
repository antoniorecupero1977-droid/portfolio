# Climate Change Analysis & Forecast

This project analyzes historical global temperature anomalies using NASA GISTEMP data and provides predictions for the next 50 years using two different models.

## Data Source
- NASA Goddard Institute for Space Studies (GISS) Surface Temperature Analysis (GISTEMP):  
  [https://data.giss.nasa.gov/gistemp/](https://data.giss.nasa.gov/gistemp/)

## Features
- Load and clean historical temperature anomaly data (1880 - present)
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
1. Load the latest NASA GISTEMP dataset
2. Clean and process the data
3. Generate predictions up to the year 2075
4. Save a plot (`climate_prediction_plot.png`) showing historical and predicted trends

## Model Evaluation
Both the Python script and the Jupyter Notebook include a basic statistical evaluation of the models on the historical dataset (1880–present).  
The following metrics are computed for both **linear** and **polynomial** regression:

- **R² (Coefficient of Determination)** → how much variance in the data is explained by the model  
- **RMSE (Root Mean Squared Error)** → average prediction error on historical data  

These values provide an indication of model fit:  
- A higher R² means the model explains the data better.  
- A lower RMSE means the predictions are closer to the observed anomalies.  

Note: Even if the polynomial model shows a better fit (higher R²), extrapolation beyond the historical range can be unstable.
These statistical forecasts should not be considered climate scenario models, but rather illustrative trend projections.

