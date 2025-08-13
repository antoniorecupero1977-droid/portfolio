
import pandas as pd
import matplotlib.pyplot as plt
import requests
from io import StringIO

# Download NASA GISTEMP data
url = "https://data.giss.nasa.gov/gistemp/tabledata_v4/GLB.Ts+dSST.csv"
response = requests.get(url)
data = StringIO(response.text)

# Load and clean data
df = pd.read_csv(data, skiprows=1)
df = df.rename(columns={"Year": "Year"})
df = df[["Year", "J-D"]].dropna()
df.columns = ["Year", "Temp_Anomaly_C"]
df["Year"] = pd.to_datetime(df["Year"], format="%Y")

# Plot
plt.figure(figsize=(10,5))
plt.plot(df["Year"], df["Temp_Anomaly_C"], label="Temperature anomaly (°C)")
plt.title("Global Temperature Anomalies (NASA GISTEMP)")
plt.xlabel("Year")
plt.ylabel("Temperature anomaly (°C)")
plt.grid(True)
plt.legend()
plt.show()
