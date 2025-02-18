# How to Check Available Runs with the alitiq Windpower API 🌤️  

The alitiq Wind API allows you to check available forecast runs for your Windpark. This endpoint provides flexibility in choosing a weather model and forecast data, ensuring your needs are met while emphasizing the **OPTIMIZED** weather model for the most accurate predictions.  

---

## Overview  

Forecast runs represent the calculations of wind energy production based on various weather models. You can query which runs are available for a specific Windpark and select the model that best suits your application.  

---

## Why Multiple Weather Models? 🤔  

alitiq offers several weather models to provide users with options tailored to their specific use cases. These models are sourced from leading global meteorological agencies, each with unique strengths for different geographical regions and forecast requirements.  

### Supported Weather Models  

| **Weather Model**       | **Provider**        | **Description**                                                                                         |  
|-------------------------|---------------------|---------------------------------------------------------------------------------------------------------|  
| **arpege**              | MeteoFrance (FR)   | ARPEGE, a regional weather model from France with a focus on European regions.                          |  
| **harmonie_dini**       | DMI (Denmark)      | HARMONIE-AROME, a high-resolution weather model tailored for Europe.                           |  
| **icon_d2**             | DWD (Germany)      | ICON-D2, a high-resolution short-term forecast model for central Europe.                                |  
| **icon_eu**             | DWD (Germany)      | ICON-EU, a regional weather model offering enhanced resolution for Europe.                              |  
| **icon_global**         | DWD (Germany)      | ICON Global, the global version of the ICON model offering comprehensive coverage.                      |  
| **optimized**           | alitiq             | (Default) Proprietary model combining strengths of various weather sources with historical performance. |  

### Why Use the OPTIMIZED Weather Model?  
The **OPTIMIZED** weather model combines the strengths of various sources and integrates localized performance data, making it our **recommended option**. It represents our best estimate for accurate and reliable wind power forecasting.  

---

## Required Parameters  

To check available forecast runs, provide the following:  

| **Parameter**   | **Type**           | **Description**                                                     | **Default** |  
|------------------|--------------------|---------------------------------------------------------------------|-------------|  
| `location_id`    | `str`             | Unique identifier of the location.                                  | None        |  
| `weather_model`  | `str` (Optional)  | Name of the weather model (e.g., `optimized`, `icon_eu`, `arpege`). | OPTIMIZED   |  

---

## Example: Check Available Runs  

Here’s how to check available forecast runs using the `forecast/check/` endpoint or the `check_available_runs` method of the python SDK:

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/wind/forecast/check/"
    
    querystring = {"weather_model":"icon_eu", "location_id": "WP123", "number_of_runs": 10}
    
    payload = ""
    headers = {"x-api-key": "api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqWindAPI
    
    # Initialize the API client
    wind_api = alitiqWindAPI(api_key="your-api-key")
    
    # Define the location ID and optional weather model
    location_id = "WP123"
    
    # Check available forecast runs
    available_runs = wind_api.check_available_runs(location_id=location_id, weather_model="optimized")
    
    # Print the available runs
    print("Available forecast runs:")
    print(available_runs)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/wind/forecast/check/?weather_model=icon_eu&location_id=WP123&number_of_runs=10' \
      --header 'x-api-key: api-key'
    ``` 



---

## API Response  

The response includes the list of available forecast runs:  

```json
{
	"weather_model": "icon_eu",
	"time": "2025-02-18T05:47:24.347131",
	"dt_calcs": [
		"2024-12-02T06:00:00",
		"2024-12-02T00:00:00",
		"2024-12-01T18:00:00",
		"2024-12-01T12:00:00",
		"2024-12-01T06:00:00",
		"2024-12-01T00:00:00",
		"2024-11-30T18:00:00",
		"2024-11-30T12:00:00",
		"2024-11-30T06:00:00",
		"2024-11-30T00:00:00"
	],
	"location_id": [
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz",
		"EP_Serbitz"
	]
} 
```  

---

## Best Practices  

- **Choose the OPTIMIZED Model**: While other models may suit specific needs, we strongly recommend the **OPTIMIZED** model for its superior accuracy.  
- **Verify Run Availability**: Always check the available runs before attempting to retrieve forecast data to ensure data freshness.  
- **Use Recent Runs**: For better accuracy, use the most recent run available.  

---

## Notes  

- **Custom Weather Models**: Specify other models like `arpege` or `icon-global` if needed for specific comparisons or analyses.  
- **Data Freshness**: New runs are typically generated at regular intervals; check often for updates.  
- **Optimized Performance**: The API is designed to handle large portfolios, ensuring that checking runs for multiple locations is efficient.  

---

For further assistance, reach out to [support@alitiq.com](mailto:support@alitiq.com). 🌟  