# Accessing Forecasts with the alitiq Load API  

The alitiq Load API provides robust and flexible forecasting capabilities for individual timeseries and entire portfolios. This guide walks you through retrieving forecasts and explains the parameters that allow you to tailor the output to your specific needs.

---

## Features 🌟  

- **Flexibility in Forecasting**: Customize forecasts using parameters such as time zone, interval, and power measurement.  
- **Asset-Level Forecasting**: Retrieve precise forecasts for individual Load timeseries.  
- **Time-Specific Forecasts**: Fetch forecasts calculated at specific times (`dt_calc`) for advanced planning.  
- **Easy Access & Integration**: By using your own location identifier it is easy to access the right forecasts and  integrate it into your system

---

## Forecasting for a Single Load timeseries

To access a forecast for a specific Solar PV system, use the `forecast/` endpoint from the API or the `get_forecast` method from the SDK.

### Example  

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/load/forecast/"
    
    querystring = {"location_id":"123","response_format":"html", "timezone":"UTC","power_measure":"kW","interval_in_minutes":"15"}
    
    payload = ""
    headers = {"x-api-key": "your-api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from datetime import datetime
    from alitiq import alitiqLoadAPI
    
    # Initialize the Solar API client
    load_api = alitiqLoadAPI(api_key="your-api-key")
    
    # Retrieve forecast for a specific Solar PV system
    forecast = load_api.get_forecast(
        location_id="99",  # Replace with your system's location ID
        dt_calc=datetime(2024, 6, 15, 12),  # Optional: specify the calculation timestamp
        power_measure="kW",  # Specify the power measurement unit
        timezone="UTC",  # Set the timezone
        interval_in_minutes=15,  # Set the forecast interval
        window_boundary="end"  # Define how intervals are calculated
    )
    
    # Display the forecast
    print(forecast)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/load/forecast/?location_id=99&response_format=json&timezone=UTC&power_measure=kW&interval_in_minutes=15' \
      --header 'x-api-key: your-api-key'
    ``` 


---

## Understanding Forecast Parameters  

The following parameters offer you flexibility when generating forecasts:  

| **Parameter**           | **Description**                                                                                                 | **Default Value**  |
|--------------------------|-----------------------------------------------------------------------------------------------------------------|--------------------|
| `location_id`           | Unique identifier for the Solar PV system. Required for system-level forecasts. This is your defined identifer. | *None*            |
| `dt_calc`               | Timestamp for forecast calculation. Useful for time-specific forecasts, and access historic ones.               | *Latest available*|
| `power_measure`         | Unit of power measurement (`kW`, `MW`, etc.).                                                                   | `"kW"`            |
| `timezone`              | Timezone for the forecast data.                                                                                 | `"UTC"`           |
| `interval_in_minutes`   | Forecast interval (e.g., `15` for 15-minute intervals). Important for retieviing Energy instead of Power        | `15`              |
| `window_boundary`       | Defines interval boundaries (`begin`, `center`, or `end`).                                                      | `"end"`           |

---

## Flexibility as a Feature  

The flexibility to define parameters ensures that the API adapts to various use cases, whether you need:  

- Forecasts for specific systems.  
- Customized intervals and time zones.  
- Tailored outputs based on specific power measurement units.  

This adaptability makes the alitiq Solar API a powerful tool for energy planning and decision-making.  

---

## Support  

For further assistance, contact [support@alitiq.com](mailto:support@alitiq.com). 🌞  