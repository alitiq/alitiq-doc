# How to Check Available Runs with the alitiq Solar API 🌤️  

The alitiq Solar API allows you to check available forecast runs for your Solar PV systems. This endpoint provides flexibility in choosing a weather model and forecast data, ensuring your needs are met while emphasizing the **OPTIMIZED** weather model for the most accurate predictions.  

---

## Overview  

Forecast runs represent the calculations of solar energy production based on various weather models. You can query which runs are available for a specific Solar PV system and select the model that best suits your application.  

---

## Why Multiple Weather Models? 🤔  

alitiq offers several weather models to provide users with options tailored to their specific use cases. These models are sourced from leading global meteorological agencies, each with unique strengths for different geographical regions and forecast requirements.  

### Supported Weather Models  

| **Weather Model**       | **Provider**        | **Description**                                                                                         |  
|-------------------------|---------------------|---------------------------------------------------------------------------------------------------------|  
| **ncep_gfs_025**        | NCEP (USA)         | Global Forecast System (GFS), providing global coverage with reliable accuracy.                         |  
| **arpege**              | MeteoFrance (FR)   | ARPEGE, a regional weather model from France with a focus on European regions.                          |  
| **harmonie_dini**       | DMI (Denmark)      | HARMONIE-AROME, a high-resolution weather model tailored for Europe.                           |  
| **metoffice_um_global** | Met Office (UK)    | Unified Model (UM) Global, offering accurate forecasts with broad coverage.                             |  
| **icon_d2**             | DWD (Germany)      | ICON-D2, a high-resolution short-term forecast model for central Europe.                                |  
| **icon_eu**             | DWD (Germany)      | ICON-EU, a regional weather model offering enhanced resolution for Europe.                              |  
| **icon_global**         | DWD (Germany)      | ICON Global, the global version of the ICON model offering comprehensive coverage.                      |  
| **optimized**           | alitiq             | (Default) Proprietary model combining strengths of various weather sources with historical performance. |  

### Why Use the OPTIMIZED Weather Model?  
The **OPTIMIZED** weather model combines the strengths of various sources and integrates localized performance data, making it our **recommended option**. It represents our best estimate for accurate and reliable solar energy forecasting.  

---

## Required Parameters  

To check available forecast runs, provide the following:  

| **Parameter**   | **Type**           | **Description**                                                           | **Default** |  
|------------------|--------------------|---------------------------------------------------------------------------|-------------|  
| `location_id`    | `str`             | Unique identifier of the location.                                        | None        |  
| `weather_model`  | `str` (Optional)  | Name of the weather model (e.g., `optimized`, `icon_eu`, `ncep_gfs_025`). | OPTIMIZED   |  

---

## Example: Check Available Runs  

Here’s how to check available forecast runs using the `forecast/check/` endpoint or the `check_available_runs` method of the python SDK:

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/solar/forecast/check/"
    
    querystring = {"weather_model":"icon_eu", "location_id": "1", "number_of_runs": 10}
    
    payload = ""
    headers = {"x-api-key": "api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqSolarAPI
    
    # Initialize the API client
    solar_api = alitiqSolarAPI(api_key="your-api-key")
    
    # Define the location ID and optional weather model
    location_id = "SP123"
    
    # Check available forecast runs
    available_runs = solar_api.check_available_runs(location_id=location_id, weather_model="optimized")
    
    # Print the available runs
    print("Available forecast runs:")
    print(available_runs)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/solar/forecast/check/?weather_model=icon_eu&location_id=1&number_of_runs=10' \
      --header 'x-api-key: api-key'
    ``` 



---

## API Response  

The response includes the list of available forecast runs:  

```plaintext
|      run_id      |  dt_run_start   |  dt_forecast_start  | weather_model   |  
|-------------------|-----------------|---------------------|-----------------|  
| 00123456789abcdef | 2024-06-10T08:00| 2024-06-10T10:00    | optimized       |  
| 00123456789ghijkl | 2024-06-10T14:00| 2024-06-10T16:00    | icon-eu         |  
```  

---

## Best Practices  

- **Choose the OPTIMIZED Model**: While other models may suit specific needs, we strongly recommend the **OPTIMIZED** model for its superior accuracy.  
- **Verify Run Availability**: Always check the available runs before attempting to retrieve forecast data to ensure data freshness.  
- **Use Recent Runs**: For better accuracy, use the most recent run available.  

---

## Notes  

- **Custom Weather Models**: Specify other models like `meteofrance_arpege` or `icon-global` if needed for specific comparisons or analyses.  
- **Data Freshness**: New runs are typically generated at regular intervals; check often for updates.  
- **Optimized Performance**: The API is designed to handle large portfolios, ensuring that checking runs for multiple locations is efficient.  

---

For further assistance, reach out to [support@alitiq.com](mailto:support@alitiq.com). 🌟  