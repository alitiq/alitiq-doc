# Accessing Forecasts with the alitiq Windpower API  

The alitiq Wind API provides robust and flexible forecasting capabilities for individual Windparks and entire portfolios. This guide walks you through retrieving forecasts and explains the parameters that allow you to tailor the output to your specific needs.

---

## Features 🌟  

- **Flexibility in Forecasting**: Customize forecasts using parameters such as timezone (`tz`), interval, and power measurement.  
- **System-Level Forecasting**: Retrieve precise forecasts for individual Windparks ( aka. locations).  
- **Portfolio-Level Forecasting**: Aggregate forecasts for your entire portfolio in one request.  
- **Time-Specific Forecasts**: Fetch forecasts calculated at specific times (`dt_calc`) for advanced planning.  
- **Easy Access & Integration**: By using your own location identifier it is easy to access the right forecasts and  integrate it into your system

---

## Forecasting for a Single Windpark

To access a forecast for a specific Windpark, use the `forecast/single/` endpoint from the API or the `get_forecast` method from the SDK.

### Example  

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/wind/forecast/single/"
    
    querystring = {"location_id":"WP123","response_format":"html","weather_model":"icon_eu","timezone":"UTC","power_measure":"kW","interval_in_minutes":"15"}
    
    payload = ""
    headers = {"x-api-key": "your-api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from datetime import datetime
    from alitiq import alitiqWindAPI
    
    # Initialize the Wind API client
    wind_api = alitiqWindAPI(api_key="your-api-key")
    
    # Retrieve forecast for a specific WindPark
    forecast = wind_api.get_forecast(
        location_id="WP123",  # Replace with your system's location ID
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
      --url 'https://api.alitiq.com/wind/forecast/single/?location_id=123&response_format=json&weather_model=icon_eu&timezone=UTC&power_measure=kW&interval_in_minutes=15' \
      --header 'x-api-key: your-api-key'
    ``` 


---

## Forecasting for an Entire Portfolio  

To access a forecast for your whole portfolio of PV systems, use the `forecast/portfolio/` endpoint from the API or the `get_forecast_portfolio` method from the SDK.

### Example  



=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/wind/forecast/portfolio/"
    
    querystring = {"response_format":"html","weather_model":"icon_eu","timezone":"UTC","power_measure":"kW","interval_in_minutes":"15", "portfolio_sum_column":"False"}
    
    payload = ""
    headers = {"x-api-key": "your-api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from datetime import datetime
    from alitiq import alitiqWindAPI
    
    # Initialize the Wind API client
    wind_api = alitiqWindAPI(api_key="your-api-key")
    
    # Retrieve portfolio-wide forecast
    portfolio_forecast = wind_api.get_forecast_portfolio(
        dt_calc=datetime(2024, 6, 15, 12),  # Optional: specify the calculation timestamp
        power_measure="kW",  # Specify the power measurement unit
        timezone="UTC",  # Set the timezone
        interval_in_minutes=15,  # Set the forecast interval
        window_boundary="end",  # Define how intervals are calculated
        portfolio_sum_column=True  # Optionally include a column summing all systems
    )
    
    # Display the portfolio forecast
    print(portfolio_forecast)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/wind/forecast/portfolio/?response_format=csv&weather_model=icon_eu&timezone=UTC&power_measure=kW&interval_in_minutes=15' \
      --header 'x-api-key: your-api-key'
    ```

---

## Understanding Forecast Parameters  

The following parameters offer you flexibility when generating forecasts:  

| **Parameter**           | **Description**                                                                                          | **Default Value**  |
|--------------------------|----------------------------------------------------------------------------------------------------------|--------------------|
| `location_id`           | Unique identifier for the WindPark. Required for system-level forecasts. This is your defined identifer. | *None*            |
| `dt_calc`               | Timestamp for forecast calculation. Useful for time-specific forecasts, and access historic ones.        | *Latest available*|
| `power_measure`         | Unit of power measurement (`kW`, `MW`, etc.).                                                            | `"kW"`            |
| `timezone`              | Timezone for the forecast data.                                                                          | `"UTC"`           |
| `interval_in_minutes`   | Forecast interval (e.g., `15` for 15-minute intervals). Important for retieviing Energy instead of Power | `15`              |
| `window_boundary`       | Defines interval boundaries (`begin`, `center`, or `end`).                                               | `"end"`           |
| `portfolio_sum_column`  | Adds a column summing forecasts for all systems in the portfolio.                                        | `True`            |

---

## Flexibility as a Feature  

The flexibility to define parameters ensures that the API adapts to various use cases, whether you need:  

- Forecasts for specific systems.  
- Aggregated data for an entire portfolio.  
- Customized intervals and time zones.  
- Tailored outputs based on specific power measurement units.  
- Easy integration by using your own identifiers

This adaptability makes the alitiq Wind API a powerful tool for energy planning and decision-making.  

---

## Support  

For further assistance, contact [support@alitiq.com](mailto:support@alitiq.com). 🌞  