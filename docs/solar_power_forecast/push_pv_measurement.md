# Pushing Measurements to the alitiq Solar API 📊  

This guide explains how to push measurements from a Solar PV power plant to the alitiq Solar API. Measurements are critical for enhancing forecast accuracy and for monitoring performance.  

---

## Overview  

The alitiq Solar API allows you to submit real-time or historical measurement data from your Solar PV systems. Each measurement includes details about the time of recording, power output, and additional optional information like irradiance.  

### Key Features ✨  
- **Real-time Measurements**: Submit live data for improved forecast accuracy.  
- **Historical Measurements**: Push past data for performance analysis and enhanced forecasting.  
- **Optimized Forecasting**: With historical measurement data of up to 90 days, the API provides highly optimized forecasts tailored to your PV system.  
- **Flexible Time Intervals**: Define custom intervals for measurements (e.g., 15 minutes).  

---

## Required Measurement Data  

When pushing measurements, you need to include the following information:  

| **Field**            | **Type**         | **Description**                                                   | **Default**    |  
|-----------------------|------------------|-------------------------------------------------------------------|----------------|  
| `location_id`         | `str`           | Unique ID of the location where the measurement was recorded.     | None           |  
| `dt`                 | `datetime`      | Timestamp of the measurement (ISO 8601 format).                   | None           |  
| `power`              | `float`         | Power output recorded (in specified unit).                        | None           |  
| `irradiance`         | `float`         | (Optional) Irradiance value in W/m².                              | `-1.0`         |  
| `power_measure`      | `str`           | Unit of power measurement (`kW`, `W`, etc.).                      | `kW`           |  
| `timezone`           | `str`           | Timezone of the measurement data.                                 | `UTC`          |  
| `interval_in_minutes` | `int`           | Interval between measurements (in minutes).                       | `15`           |  
| `window_boundary`    | `str`           | Defines the interval's alignment (`begin`, `center`, or `end`).    | `end`          |  

---

## Note on Historical Measurements  

To provide highly optimized forecasts, the API requires at least 90 days of historical measurement data for a given Solar PV system. This data enables the system to fine-tune forecasts to match the unique characteristics of your setup.  This data needs to updated once per day for the last 24 hours. In case of diurnal updates, alitiq will adapt the forecast tot the latest observations every 15 minutes. 

---

## Example Code to Push Measurements  

Here’s an example demonstrating how to submit measurement data using the `measurement/add` endpoint and the python-SDK method `post_measurements`:


=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/solar/measurement/add/"
    
    payload = [
        {
            "location_id": "2",
            "dt": "2022-03-06T09:45:00.000",
            "power": 201,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:00:00.000",
            "power": 213,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:15:00.000",
            "power": 242,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:30:00.000",
            "power": 270,
            "irradiance": 234,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:45:00.000",
            "power": 320,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T11:00:00.000",
            "power": 397,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        }
    ]
    headers = {"Content-Type": "application/json", "x-api-key": {api-key}}
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from datetime import datetime
    from alitiq import alitiqSolarAPI, PvMeasurementForm
    
    # Initialize the API client
    solar_api = alitiqSolarAPI(api_key="your-api-key")
    
    # Create measurement data
    pv_measurements = [
        PvMeasurementForm(
            location_id="SP123",
            dt=datetime(2024, 6, 10, 10).isoformat(),
            power=120.5,
            power_measure="kW",
            timezone="UTC",
            interval_in_minutes=15,
            window_boundary="end",
        ),
        PvMeasurementForm(
            location_id="SP123",
            dt=datetime(2024, 6, 10, 10, 15).isoformat(),
            power=90.8,
            power_measure="kW",
            timezone="UTC",
            interval_in_minutes=15,
            window_boundary="end",
        ),
        PvMeasurementForm(
            location_id="SP123",
            dt=datetime(2024, 6, 10, 10, 30).isoformat(),
            power=150.0,
            power_measure="kW",
            timezone="UTC",
            interval_in_minutes=15,
            window_boundary="end",
        ),
    ]
    
    # Push measurements to the API
    response = solar_api.post_measurements(pv_measurements)
    
    # Print the API response
    print("API Response:", response)
    ```

=== "cURL"

    ``` bash
    curl --request POST \
      --url https://api.alitiq.com/solar/measurement/add/ \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: {api-key}' \
      --data '[
        {
            "location_id": "2",
            "dt": "2022-03-06T09:45:00.000",
            "power": 201.0,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:00:00.000",
            "power": 213.0,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:15:00.000",
            "power": 242.0,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:30:00.000",
            "power": 270.0,
            "irradiance": 234.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T10:45:00.000",
            "power": 320,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": "2",
            "dt": "2022-03-06T11:00:00.000",
            "power": 397,
            "irradiance": -1,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        }
    ]'
    ```

---



---

## API Response  

- A successful request will return a confirmation message indicating the data was received and processed.  
- If there are validation errors (e.g., missing fields, incorrect formats), the API will return an error message with details.  

---

## Notes on Best Practices  

- **Batch Submissions**: Push multiple measurements in a single API call for efficiency.  
- **Time Synchronization**: Ensure timestamps (`dt`) are accurate and in the correct timezone.  
- **Historical Data**: Provide at least 90 days of measurements to unlock optimized forecasting.  
- **Validation**: Use the SDK's `PvMeasurementForm` for automatic data validation.  

---

For further assistance, please reach out to [support@alitiq.com](mailto:support@alitiq.com). 🌟  