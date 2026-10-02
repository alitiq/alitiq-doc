# ☀️ **Irradiance Observations API**

This API provides **solar irradiance observations** derived from the **MSG satellite** (Meteosat Second Generation), covering Europe and Africa (full disk view).

It allows you to query irradiance time series for a given point location, either by coordinates, city name, or zip code, over a specified time range.

---

## 🌍 **Spatial Coverage**

* **Source**: EUMETSAT CM-SAF data processed and delivered by DWD
* **Coverage**: Europe, Africa, and the surrounding MSG full-disk view
* **Resolution**: Point location queried from satellite gridded irradiance data

---

## 📥 **API Endpoint**

`GET https://api.alitiq.com/weather/irradiance`

---

## 🔑 **Query Parameters**

| Parameter         | Type   | Description                                               |
| ----------------- | ------ | --------------------------------------------------------- |
| `latitude`        | float  | Latitude of the point (optional if city or zip provided)  |
| `longitude`       | float  | Longitude of the point (optional if city or zip provided) |
| `zip_code`        | string | Optional zip code (used if coordinates not provided)      |
| `city_name`       | string | Optional city name (used if coordinates not provided)     |
| `start_date`      | string | Start datetime (ISO format, e.g., `2024-05-01T00:00`)     |
| `end_date`        | string | End datetime (ISO format, e.g., `2024-05-01T03:00`)       |
| `satellite`       | string | `cm_saf_europe` (default, 10-minute values from 2026-07-10) or `cm_saf` (15-minute values) |
| `response_format` | string | `json`, `csv`, or `html` (default: `json`)                |

---

## 📦 **Returned Data**

* **Variable**:
  `global_horizontal_irradiance` → measured in **W/m²**
* **Interval**: \~15-minute values over the requested time period
* **Output format**: JSON, CSV, or HTML time series plot

---

## ⚠️ **Important Notes**

✅ Data is based on satellite-derived estimates, not ground station measurements
✅ Only available for locations within the MSG satellite full-disk view (Europe, Africa)
✅ If using `zip_code` or `city_name`, the service will geocode the location to coordinates
✅ To simulate the power output of a PV system from these observations, see [PV simulation from irradiance](pv_simulation.md)

---

## 🔧 **Example Request**

=== "python requests"

    ```python
    import requests
    import pandas as pd
    from io import BytesIO
    
    url = "https://api.alitiq.com/weather/irradiance/"
    
    querystring = {"latitude":47.99444,"longitude":10.692917,"response_format":"json"}
    payload = ""
    headers = {"x-api-key": "your-api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    data = pd.read_json(BytesIO(response.content), orient='split')
    ```


=== "cURL"

    ```bash
    curl --request GET \
      --header 'x-api-key: {api-key}' \
      --url 'https://api.alitiq.com/weather/irradiance?latitude=48.8566&longitude=2.3522&start_date=2025-05-01T06:00&end_date=2025-05-01T12:00&response_format=json'
    ```
