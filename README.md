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

⚠️ Note: Even if the polynomial model shows a better fit (higher R²), extrapolation beyond the historical range can be unstable. These statistical forecasts should not be considered climate scenario models, but rather illustrative trend projections.

## Results Interpretation
Based on the evaluation metrics obtained:

- **Linear Regression**:  
  - R² ≈ 0.76 → explains ~76% of the variability in the historical data  
  - RMSE ≈ 0.19°C → average prediction error on historical anomalies  
  - Captures the long-term trend but underestimates recent acceleration

- **Polynomial Regression (degree 3)**:  
  - R² ≈ 0.91 → explains ~91% of the variability, significantly better fit  
  - RMSE ≈ 0.12°C → lower average error  
  - Follows more closely the recent upward trend

### Takeaway
- The polynomial model statistically fits the past data better.  
- The linear model is simpler and more stable but less accurate in describing recent decades.  
- ⚠️ Extrapolation beyond the historical range (after 2025) should be interpreted cautiously, especially for the polynomial model. These results are illustrative and **not a substitute for physics-based climate projections (e.g., CMIP/IPCC scenarios)**.
