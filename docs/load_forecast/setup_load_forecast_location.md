# Load power forecasting locations

Welcome to the **alitiq Load Forecasting API**! This guide explains how to create and list **load locations** (e.g., sites, meters, buildings) that receive electricity load forecasts.

---

## Key concepts 📚

In the **alitiq Load API**, a **load location** represents a place where you want forecasts (e.g., a single meter, a campus, or a substation).
Each location has a human-friendly **external ID** (what *you* use) and an internal ID (what *we* store). The API maps internal IDs back to your external IDs for every response.

**Location fields**

| Field                       |     Type | Required | Notes                                                                        |
| --------------------------- | -------: | :------: | ---------------------------------------------------------------------------- |
| `site_name`                 |   string |     ✅    | Display name of the location.                                                |
| `service`                   |   enum   |     ⭕    | Which kind of timeseries/service. If omitted: set to electricity-load        |
| `location_id`               |   string |     ⭕    | Your **external** identifier. If omitted, the API assigns one automatically. |
| `latitude`                  |    float |     ✅    | Decimal degrees.                                                             |
| `longitude`                 |    float |     ✅    | Decimal degrees.                                                             |
| `reference_weather_station` |      int |     ❌    | **Ignored on create**; server overwrites to `9999`.                          |
| `created_at`                | datetime |     ❌    | Set by server at creation time (UTC).                                        |

---

## Services ⚡🔥💨

Each location must belong to one **service type**. This defines which forecasting engine is applied.

| Service              | Enum value         | Description                                                  |
| -------------------- | ------------------ | ------------------------------------------------------------ |
| **Electricity Load** | `electricity-load` | Forecast electricity consumption (default if not specified). |
| **District Heating** | `district-heating` | Forecast thermal load for heating networks.                  |
| **Gas Load**         | `gas_load`         | Forecast natural gas demand.                                 |
| **Grid Loss**        | `grid-loss`        | Forecast electrical grid losses.                             |
| **Regional Wind**    | `regional-wind`    | Forecast aggregated wind generation for a region.            |
| **Regional Solar**   | `regional-solar`   | Forecast aggregated solar generation for a region.           |
| **Regional Load**    | `regional-load`    | Forecast aggregated electricity demand for a region.         |

> If omitted, the API sets `service = electricity-load`.



## Add a new load location 🚀

Use `load/location/add/` to create a single load location.

=== "python requests"

    ```python
    import requests

    url = "https://api.alitiq.com/load/location/add/"
    headers = {
        "Content-Type": "application/json",
        "x-api-key": "{api-key}",
    }

    payload = {
        "site_name": "HQ Campus",
        "location_id": "HQ-001",   # optional; omit to auto-assign
        "latitude": 52.520008,
        "longitude": 13.404954,
        # "service": "gas-load",  # optional; omit default is electricity-load
    }

    resp = requests.post(url, json=payload, headers=headers)
    print(resp.status_code)  # 201 on success
    print(resp.json())       # {"location_id": "HQ-001", "site_name": "HQ Campus"}
    ```
=== "alitiq-py"

    ```python
    from alitiq.models.load_forecast import LoadLocationForm

    # Example
    api = alitiqLoadAPI(api_key="your-key")

    location = LoadLocationForm(
        site_name="HQ Campus",
        location_id="HQ-001",
        latitude=52.52,
        longitude=13.405,
        service="gas-load",  # default electricity-load
    )

    resp = api.create_location(location)
    print(resp)
    ```

=== "cURL"

    ```bash
    curl --request POST \
    --url https://api.alitiq.com/load/location/add/ \
    --header 'Content-Type: application/json' \
    --header 'x-api-key: {api-key}' \
    --data '{
        "site_name": "HQ Campus",
        "location_id": "HQ-001",
        "latitude": 52.520008,
        "longitude": 13.404954
    }'
    ```

**Successful response**

```json
{
  "location_id": "HQ-001",
  "site_name": "HQ Campus"
}
```

> If you omit `location_id`, the API assigns one and returns it in the response.

---

## Inspect your portfolio 📋

Use `load/location/list/` to retrieve all your load locations.
Choose your preferred response format via `?response_format=...`:

* `json`
* `html`
* `csv`

=== "python requests (JSON)"

    ```python
    import requests

    url = "https://api.alitiq.com/load/location/list/"
    params = {"response_format": "json"}
    headers = {"x-api-key": "{api-key}"}

    resp = requests.get(url, params=params, headers=headers)
    print(resp.json())
    ```

=== "python requests (HTML)"

    ```python
    import requests

    url = "https://api.alitiq.com/load/location/list/"
    params = {"response_format": "html"}
    headers = {"x-api-key": "{api-key}"}

    resp = requests.get(url, params=params, headers=headers)
    print(resp.text)  # ready-to-render HTML table
    ```

=== "alitiq-py"

    ```python
    from alitiq.models.load_forecast import LoadLocationForm

    # Example
    load_api = alitiqLoadAPI(api_key="your-key")

    response = solar_api.list_locations()
    print("Locations:", response)
    ```

=== "cURL (CSV)"

    ```bash
    curl --request GET \
    --url 'https://api.alitiq.com/load/location/list/?response_format=csv' \
    --header 'x-api-key: {api-key}'
    ```

**Example JSON response**

```json
{
  "columns": [
    "location_id",
    "site_name",
    "latitude",
    "longitude",
    "reference_weather_station",
    "service",
    "created_at"
  ],
  "index": [0, 1],
  "data": [
    ["HQ-001", "HQ Campus", 52.520008, 13.404954, 9999, "ELECTRICITY_LOAD", "2025-08-19T09:31:12+00:00"],
    ["PLANT-A", "Manufacturing Plant A", 48.1351, 11.5820, 9999, "ELECTRICITY_LOAD", "2025-08-18T15:07:45+00:00"]
  ]
}
```


> The `location_id` shown here is always your **external** ID. The API performs the internal↔external mapping automatically.

**HTML view**

When `response_format=html`, the endpoint returns a styled `<table>` suitable for dashboards and documentation.

---

## Behavior & validations ⚙️

* **Reference weather station**: Any value provided on create is **overwritten** by the server (`9999`). You can omit it.
* **Timestamps**: `created_at` is set server-side using UTC.
* **Notifications**: A backoffice notification is triggered when a new location is created (no action needed from you).
* **Services**: Defaults to `electricity-load` and typically doesn’t need to be set.

---

## Errors ❗

| Scenario                         | Status | Body (example)                                                               |
| -------------------------------- | :----: | ---------------------------------------------------------------------------- |
| Unsupported `response_format`    |   401  | `{ "detail": { "error": "INVALID_RESPONSE_FORMAT", ... } }`                  |
| Invalid configuration (creation) |   401  | `{ "detail": { "error": "INVALID_SYSTEM_CONFIG", "error_message": "..." } }` |

---

## FAQs ❓

### Do I have to provide a `location_id`?

No. If you omit it, the API assigns one and returns it. You’ll also see it in `list/`.

### Can I update or delete a load location?

Updates are not yet available. A delete endpoint is planned but currently disabled.

### Why is `reference_weather_station` always 9999?

It’s managed by alitiq and currently fixed to ensure consistent model input. You can ignore this field when creating locations.

---

## Endpoint reference 📑

* **Create:** `POST https://api.alitiq.com/load/location/add/`
  **Body:** `{ "site_name": str, "location_id": str?, "latitude": float, "longitude": float }`
  **Returns:** `201 Created` with `{"location_id": str, "site_name": str}`

* **List:** `GET https://api.alitiq.com/load/location/list/?response_format={json|html|csv}`
  **Returns:** Table of locations (format as requested)

---

## Support & feedback 💬

* **Contact:** [support@alitiq.com](mailto:support@alitiq.com)

🌟 **Start forecasting smarter with alitiq today!** 🌟
