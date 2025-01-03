---
date: 2024-11-22
authors: [alitiq]
categories:
  - Evaluation
  - Metrics
  - Forecast
  - Accuracy
---
# How to Evaluate Forecasts for the Energy Sector in 2024 🔍⚡📊

Forecasting is a cornerstone of the energy sector, enabling decision-making for operations, investments, and policy development. However, the real value of a forecast lies in its evaluation and cross-validation. How well did it predict reality? 
Here’s a step-by-step guide to evaluating forecasts, focusing on understanding the process, selecting the right forecasts, and comparing them against observations.

<!-- more -->


---

## 🌟 **1. Understand the Process**: Decision-Making Context 📅🧠

Before diving into evaluation, it’s crucial to understand *why* the forecast was made and what kind of **forecast horizon** we need to target this. This context is key to interpreting the results correctly. In general you can differ between three different kind of forecast in the energy industry overall: 

- **Operational Forecasts**: Short-term, used for managing daily grid operations or scheduling energy dispatch.
- **Market Forecasts**: Medium-term, help with bidding strategies or setting tariffs.
- **Strategic Forecasts**: Long-term, guide investment decisions like building renewable plants or expanding infrastructure.

By clarifying the decision-making context and forecast horizon upfront, you can set the right expectations for evaluation. 

---

## 📂 **2. Select Forecasts for Evaluation**: What and When? 🧾

Energy systems generate forecasts at multiple time steps and for various variables (e.g., demand, generation, prices). Evaluating them all can be overwhelming, so **filter relevant forecasts** based on:

1. **Variable of Interest**: E.g., electricity demand, wind power, spot prices.
2. **Horizon & Timing**: Only forecasts relevant to your **decision-making window** should be considered.
3. **Availability of Observations**: You need actual data (ground truth) to evaluate forecasts.

### Example: Selecting Forecasts to Evaluate
```python
# Filter forecasts for evaluation
forecasts = pd.DataFrame({
    "calculation_timestamp": ["2024-11-17", "2024-11-17", "2024-11-17"],
    "timestamp": ["2024-11-17", "2024-11-18", "2024-11-19"],
    "forecasted_demand": [1000, 1050, 1100],
    "observed_demand": [1020, 1040, 1095]
})

# Focus on dates within the day-ahead horizon, according to the given calculation timestamp at 17th of novembre: 
start_date = "2024-11-18"
end_date = "2024-11-19"

filtered_forecasts = forecasts[
    (forecasts["timestamp"] >= start_date) & (forecasts["timestamp"] <= end_date)
]

print(filtered_forecasts)
```

This step ensures you’re only working with forecasts that are meaningful and can be tested against real data.

---

## 📊 **3. Evaluate Forecasts Against Observations**: Metrics & Tools 📈📉

With the relevant forecasts in hand, the next step is to calculate **forecast accuracy** or **error metrics** by comparing predictions to actual observations. Common metrics include:

- **Mean Absolute Error (MAE)**: Average absolute difference between forecasts and observations. Should be used with a normalization only, otherwise it will overweight low valued errors. 
- **Root Mean Square Error (RMSE)**: Emphasizes larger errors, useful for operational reliability. This is the most powerful metric
- **Bias**: Average over- or under-prediction. Really helpful to understand e.g. optimisation potential, as systematic errors are much easier to vanish. Your forecast should be bias free in any case.  

### Example: Calculating Error Metrics
```python
import numpy as np

# Calculate error metrics
filtered_forecasts["error"] = (
    filtered_forecasts["forecasted_demand"] - filtered_forecasts["observed_demand"]
)

# Metrics
mae = np.mean(abs(filtered_forecasts["error"]))
rmse = np.sqrt(np.mean(filtered_forecasts["error"]**2))
mape = np.mean(abs(filtered_forecasts["error"] / filtered_forecasts["observed_demand"])) * 100

print(f"MAE: {mae:.2f}, RMSE: {rmse:.2f}, MAPE: {mape:.2f}%")
```

Output:
```
MAE: 10.00, RMSE: 10.44, MAPE: 0.94%
```

These metrics quantify how close the forecasts were to the observed values and highlight areas for improvement.

---

## 🔁 **4. Iterative Refinement**: Learn & Improve 🚀

Forecast evaluation is not a one-and-done task. Use insights from evaluation to refine your models or forecasting processes:

1. **Investigate Bias**: If forecasts are consistently over- or under-predicting, revisit assumptions or inputs.
2. **Tailor Horizons**: Maybe different horizons need distinct models.
3. **Collaborate**: Feedback loops between forecasters and decision-makers can ensure alignment.

---

## 🛠 Tools for Forecast Evaluation 📌

Python libraries like **pandas**, **numpy**, and **scikit-learn** are great for quick evaluations. For advanced needs, explore:

- **`statsmodels`**: Time series analysis and evaluation. Test stationarity and seasonality. 
- **`forecast-tools`**: Pre-built utilities for energy forecasting.
- **`matplotlib`** or **`seaborn`**: Visualization to uncover patterns or anomalies.

---

## 🏁 Conclusion

Evaluating energy sector forecasts isn’t just about crunching numbers—it’s about understanding the decision context, selecting relevant forecasts, and applying the right metrics. By following a structured approach, you can ensure forecasts serve their ultimate purpose: empowering smart decisions. 🎯✨

Got any tips or favorite metrics? Share them in the comments below! 👇