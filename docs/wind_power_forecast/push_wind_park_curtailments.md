# Managing Unavailability via the alitiq Windpower API ⚡

This guide explains how to push **curtailments** to the alitiq Wind API for wind parks. Curtailments represent reduced power production due to grid constraints, maintenance, or market-driven limitations.

---

## Overview

The alitiq Wind API allows you to **submit** and **inspect** curtailment/unavailability data from your windparks. This data is crucial for evaluating lost production potential and improving forecasting accuracy.

### Key Features ✨
- **Real-time Curtailments/unavailability**: Push live curtailment events.  
- **Historical Curtailments/unavailability**: Submit past curtailment records for analysis.  
- **Forecast Refinement**: Curtailment/unavailability awareness improves forecast realism.  
- **Flexible Time Windows**: Define how time intervals align to your curtailment records.  

---

## Required Curtailment Data

When submitting curtailment data, include the following fields:

| **Field**            | **Type**         | **Description**                                                   | **Default**    |
|----------------------|------------------|-------------------------------------------------------------------|----------------|
| `location_id`        | `str`            | Unique ID of the wind park where the curtailment occurred.       | None           |
| `dt`                 | `datetime` or `pandas.Timestamp` | Timestamp representing the curtailment's time window.         | None           |
| `level`              | `float`          | Magnitude of curtailment (values between 0 and 1 ).          | None           |
| `timezone`           | `str`            | Timezone of the timestamp.                                        | `UTC`          |
| `interval_in_minutes` | `int`           | Interval length that the timestamp refers to.                     | `15`           |
| `window_boundary`    | `str`            | Defines alignment of `dt` (`begin`, `center`, or `end`).          | `end`          |

---

## Example Code to Push Curtailments

Use the `/wind/curtailments/add/` endpoint to submit data.

=== "python requests"

    ```python
    import requests

    url = "https://api.alitiq.com/wind/curtailments/add/"

    payload = [
        {
            "location_id": "WP001",
            "dt": "2024-06-10T10:00:00.000",
            "level": 1.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end"
        },
        {
            "location_id": "WP001",
            "dt": "2024-06-10T10:15:00.000",
            "level": 1.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end"
        }
    ]
    headers = {"Content-Type": "application/json", "x-api-key": "{your-api-key}"}

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    ```

=== "alitiq-py SDK"

    ```python
    from datetime import datetime
    from alitiq import alitiqWindAPI, CurtailmentForm

    # Initialize API client
    wind_api = alitiqWindAPI(api_key="your-api-key")

    # Create curtailment records
    curtailments = [
        CurtailmentForm(
            location_id="WP001",
            dt=datetime(2024, 6, 10, 10, 0).isoformat(),
            level=1.0,
            interval_in_minutes=15,
            timezone="UTC",
            window_boundary="end",
        ),
        CurtailmentForm(
            location_id="WP001",
            dt=datetime(2024, 6, 10, 10, 15).isoformat(),
            level=1.0,
            interval_in_minutes=15,
            timezone="UTC",
            window_boundary="end",
        ),
    ]

    # Post to the API
    response = wind_api.post_curtailments(curtailments)
    print("API Response:", response)
    ```

=== "cURL"

    ```bash
    curl --request POST \
    --url https://api.alitiq.com/wind/curtailments/add/ \
    --header 'Content-Type: application/json' \
    --header 'x-api-key: {your-api-key}' \
    --data '[
        {
            "location_id": "WP001",
            "dt": "2024-06-10T10:00:00.000",
            "level": 1.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end"
        },
        {
            "location_id": "WP001",
            "dt": "2024-06-10T10:15:00.000",
            "level": 1.0,
            "interval_in_minutes": 15,
            "timezone": "UTC",
            "window_boundary": "end"
        }
    ]'
    ```

!!! note
    You can push **up to 10,000** curtailment records in one call. It is recommended to **batch** data by month per system.

---

## API Response

- ✅ **Success**: The API returns an HTML confirmation indicating the curtailments were saved.  
- ❌ **Error**: If there's invalid input (e.g., invalid `window_boundary`), you'll receive a detailed HTTP error response.

---

## Inspecting Curtailments

You can view stored curtailments using the `/wind/curtailments/inspect/` endpoint. Supported formats:  
- `json` (default)  
- `csv`  
- `html` (generates a timeseries plot)

### Query Parameters:

| Parameter     | Type     | Description                                  |
|---------------|----------|----------------------------------------------|
| `location_id` | `str`    | External ID of the location.                 |
| `start_date`  | `str`    | Optional ISO date string.                    |
| `end_date`    | `str`    | Optional ISO date string.                    |
| `response_format` | `str` | One of `json`, `csv`, `html`.               |

---

## Notes on Best Practices
- **Mapping**: Your `location_id` must be known to alitiq—retrieved via the `get_id_locations_for_external_ids()` mapping.

- **Use `UTC`** whenever possible to ensure consistency.  
- **Window Alignment**:
    - `begin`: `dt` marks the **start** of the curtailment window  
    - `center`: `dt` is the **center** of the interval  
    - `end`: `dt` marks the **end** of the curtailment window  
- **Validation**: Use the SDK's `CurtailmentForm` for safer and structured inputs.  

---

## Contact

For help or onboarding assistance, contact: [support@alitiq.com](mailto:support@alitiq.com) 💬