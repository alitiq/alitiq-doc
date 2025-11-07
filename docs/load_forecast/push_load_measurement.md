# Pushing Measurements to the alitiq Load API 📊  

This guide explains how to push measurements from a Solar PV power plant to the alitiq Solar API. Measurements are critical for enhancing forecast accuracy and for monitoring performance.  

---

## Overview  

The alitiq Load API allows you to submit real-time or historical measurement data from your load timeseries. Each measurement includes details about the time of recording, power/load, and additional optional information like irradiance.  

### Key Features ✨  
- **Real-time Measurements**: Submit live data for improved forecast accuracy.  
- **Historical Measurements**: Push past data for performance analysis and enhanced forecasting.  
- **Flexible Time Intervals**: Define custom intervals for measurements (e.g., 15 minutes).  

---

## Required Measurement Data  

When pushing measurements, you need to include the following information:  

| **Field**            | **Type**         | **Description**                                                   | **Default**    |  
|-----------------------|------------------|-------------------------------------------------------------------|----------------|  
| `location_id`         | `str`           | Unique ID of the location where the measurement was recorded.     | None           |  
| `dt`                 | `datetime`      | Timestamp of the measurement (ISO 8601 format).                   | None           |  
| `power`              | `float`         | Power output recorded (in specified unit).                        | None           |  
| `power_measure`      | `str`           | Unit of power measurement (`kW`, `W`, etc.).                      | `kW`           |  
| `timezone`           | `str`           | (Optional) Timezone of the measurement data. Available timezones can be found **[here](https://docs.alitiq.com/utils/timezones/)                                | `None`          |  
| `interval_in_minutes` | `int`           | Interval between measurements (in minutes).                       | `15`           |  
| `window_boundary`    | `str`           | Defines the interval's alignment (`begin`, `center`, or `end`).    | `end`          |  

### Detailed explanation: 
* `timezone`: Specify the timezone of your data OR define timezone aware timestamps. Common options include:
  * Europe/Berlin (includes daylight saving time)
  * Etc/GMT-1 (standard time, no daylight saving)
  * UTC
* `window_boundary`: Define where the timestamp is located within the time window. Options are:
  * begin
  * center
  * end (default)
* `power_measure`: Specify the SI unit of your data. Available options are:
  * W
  * kW
  * MW (default)
  * MWh
  * kWh
  * Wh
* `interval_in_minutes`: Define the time interval between measurements. This is especially important if your data is in energy units rather than power.

---

## Note on Historical Measurements  

To provide highly optimized forecasts, the API requires at least 90 days of historical measurement data for a given load timeseries. This data enables the system to fine-tune forecasts to match the unique characteristics of your setup.  This data needs to updated once per day for the last 24 hours. In case of diurnal updates, alitiq will adapt the forecast tot the latest observations every 15 minutes. 


## Note on metadata:

The metadata you provide (window_boundary, power_measure) will be read only once at the moment. So changing this per entry in the payload of the request is currently not supported and will yield to wrong data in our database. 

## Allowed timestamps format

To force you to set the right timestamps we allow timezone aware OR naive timestamp with the additonal information of a timezone given for each sample in the provided data, 

The following timestamps are allowed: 

- `2025-09-08T00:00:00+00:00` : Timezone aware timestamp
- `2025-09-08T00:00:00Z` : Timezone aware timestamp, reading as UTC
- `2025-09-08T00:00:00` : Timezone naive timestamp, requires timezone parameter
- `2025-09-08T00:00:00.000` : Timezone naive timestamp, requires timezone parameter


---

## Example Code to Push Measurements  

Here’s an example demonstrating how to submit measurement data using the `measurement/add/` endpoint and the python-SDK method `post_measurements`:


=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/load/measurement/add/"
    
    payload = [
        {
            "location_id": 2,
            "dt": "2022-03-06T09:45:00.000",
            "power": 201,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:00:00.000",
            "power": 213,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:15:00.000",
            "power": 242,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:30:00.000",
            "power": 270,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:45:00.000",
            "power": 320,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T11:00:00.000",
            "power": 397,
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
    from alitiq import alitiqLoadAPI, EngineMeasurementForm
    
    # Initialize the API client
    load_api = alitiqLoadAPI(api_key="your-api-key")
    
    # Create measurement data
    load_measurements = [
        EngineMeasurementForm(
            location_id="SP123",
            dt=datetime(2024, 6, 10, 10).isoformat(),
            power=120.5,
            power_measure="kW",
            timezone="UTC",
            interval_in_minutes=15,
            window_boundary="end",
        ),
        EngineMeasurementForm(
            location_id="SP123",
            dt=datetime(2024, 6, 10, 10, 15).isoformat(),
            power=90.8,
            power_measure="kW",
            timezone="UTC",
            interval_in_minutes=15,
            window_boundary="end",
        ),
        EngineMeasurementForm(
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
    response = load_api.post_measurements(load_measurements)
    
    # Print the API response
    print("API Response:", response)
    ```

=== "cURL"

    ``` bash
    curl --request POST \
      --url https://api.alitiq.com/load/measurement/add/ \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: {api-key}' \
      --data '[
        {
            "location_id": 2,
            "dt": "2022-03-06T09:45:00.000",
            "power": 201.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:00:00.000",
            "power": 213.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:15:00.000",
            "power": 242.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:30:00.000",
            "power": 270.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T10:45:00.000",
            "power": 320,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end",
            "power_measure": "kW"
        },
        {
            "location_id": 2,
            "dt": "2022-03-06T11:00:00.000",
            "power": 397,
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

## Notes 

### Best Practices  

- **Batch Submissions**: Push multiple measurements in a single API call for efficiency.  
- **Time Synchronization**: Ensure timestamps (`dt`) are accurate and in the correct timezone. By defining `timezone`, `interval_in_minutes` and `window_boundary` we ask you to deal with it. 
- **Validation**: Use the SDK's `LoadMeasurementForm` for automatic data validation.

### Interval in minutes

The interval is important for measure transform into power (MW is default in alitiq's internal databases). Please take care that your data is aligned with the interval that you configure. 

### Window - boundary

It is important that you know where your timestamp is bounded. It can make a huge difference and will lead to timeshifts in the forecast. 
You maybe more familiar with pandas timestamp labels, so here we have mapping and a further explaination. In the future we will maybe allow for both. The examples refer to a quarter-hourly time interval:

- `begin` : `left` -> Timestamp 16:00 represents data from 16:00 to 16:15
- `center` : `center` -> Timestamp 16:07:30 represents data from 16:00 to 16:15
- `end` : `right` -> Timestamp 16:15 represents data from 16:00 to 16:15 (default in alitiq's databases)


---

For further assistance, please reach out to [support@alitiq.com](mailto:support@alitiq.com). 🌟  