# 🌧️ Precipitation data API

This API provides access to **precipitation observation data** (at 10-minute intervals) using the RADOLAN "RW" product. You can query by coordinates, zip code, or city name and retrieve data in JSON, CSV, or HTML formats.

---

## 🔗 Base URL

```
https://api.alitiq.com/weather/precipitation
```

---

## 🧾 Description

This API returns a short-term precipitation **forecast** at 10-minute intervals for a specified location and date range. Internally, it fetches hourly precipitation data from RADOLAN and derives **instant 10-minute precipitation sums** by differencing.

* **Data unit**: millimeters (mm) precipitation per 10-minute interval
* **Coverage**: entire Germany, based on the **RADOLAN grid** provided by the German Weather Service (DWD)

---

## 📥 Query Parameters

| Parameter         | Type     | Required | Description                                                |
| ----------------- | -------- | -------- | ---------------------------------------------------------- |
| `latitude`        | `float`  | Optional | Latitude of the location                                   |
| `longitude`       | `float`  | Optional | Longitude of the location                                  |
| `zip_code`        | `string` | Optional | ZIP code for location-based geocoding                      |
| `city_name`       | `string` | Optional | City name for location-based geocoding                     |
| `start_date`      | `string` | Optional | Start date (`YYYY-MM-DD`) or datetime (`YYYY-MM-DDTHH:MM`) |
| `end_date`        | `string` | Optional | End date (`YYYY-MM-DD`) or datetime (`YYYY-MM-DDTHH:MM`)   |
| `response_format` | `string` | Optional | Format of response: `json`, `csv`, or `html`               |


!!! note
    ⚠:  If `latitude` and `longitude` are not provided, you **must** provide either `zip_code` or `city_name`. They are available for Germany at the moment

---

## 🌍 Data Details

* **Spatial coverage**: Germany, following the official RADOLAN radar grid (provided by DWD)
* **Temporal resolution**: 10-minute intervals
* **Value**: precipitation sum over each 10-minute period, measured in **millimeters (mm)**

---

## 🧪 Example Requests

### Example 1: Using Coordinates

=== "python requests"

    ``` python
    import requests

    url = "https://api.alitiq.com/weather/precipitation"
    
    params = {
        "latitude": 52.52,
        "longitude": 13.405,
        "start_date": "2024-05-01T00:00",
        "end_date": "2024-05-01T03:00",
        "response_format": "json"
    }
    
    response = requests.get(url, params=params)
    
    print(response.text)

    ```

=== "cURL"

    ``` bash

    curl --request GET \
    --url 'https://api.alitiq.com/weather/precipitation?latitude=52.52&longitude=13.405&start_date=2024-05-01T00:00&end_date=2024-05-01T03:00&response_format=json'
    


    ```

=== "http"

    ```http
    GET https://api.alitiq.com/weather/precipitation?latitude=52.52&longitude=13.405&start_date=2024-05-01T00:00&end_date=2024-05-01T03:00&response_format=json
    GET https://api.alitiq.com/weather/precipitation?zip_code=10115&start_date=2024-05-01&end_date=2024-05-01&response_format=csv
    GET https://api.alitiq.com/weather/precipitation?city_name=Berlin&response_format=html
    ```

---

## 🧾 Response Formats

* **JSON** → Structured time series of 10-minute precipitation sums.
* **CSV** → Downloadable table for further data analysis.
* **HTML** → Visual plot showing precipitation over time.

---

## ⚠️ Important Notes

* The system converts hourly RADOLAN sums into **10-minute precipitation sums** by differencing.
* The most recent data has a \~30-minute delay due to radar processing.
* The RADOLAN grid provides high-resolution, radar-based precipitation data over Germany.

---

## 🔒 Authentication

Currently, the endpoint returns:

* `401 Unauthorized` → if coordinates or response format are invalid.

No user token or API key is required unless integrated separately.
