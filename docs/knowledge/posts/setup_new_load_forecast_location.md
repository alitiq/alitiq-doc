---
date: 2025-08-19
authors: [alitiq]
categories:
  - Load
---

## How to Define Load Locations in the alitiq Load Forecasting API

> \*\* Ready to start forecasting load efficiently?\*\* Setting up accurate **load locations** is the first step toward unlocking smarter demand insights—whether it's electricity, gas, or district heating.

---

<!-- more -->

### Why defining load locations matters

Every load forecast begins with a proper location setup. By defining a load location, you're telling the API *where* (geographically) and *what type* of energy demand you wish to forecast. Each location requires:

* A `site_name` for easy reference
* Coordinates (`latitude`, `longitude`)
* An optional `location_id` (your external identifier)

Once configured, you can submit measurements, retrieve forecasts, and seamlessly integrate data into your systems.

---

### Step-by-step: Add a Load Location

Here's how you set up a new location using the API.

#### Using Python (with `requests`):

```python
import requests

url = "https://api.alitiq.com/load/location/add/"
headers = {
    "Content-Type": "application/json",
    "x-api-key": "{your-api-key}",
}

payload = {
    "site_name": "Facility A",
    "location_id": "FAC-A",       # optional external ID
    "latitude": 48.1351,
    "longitude": 11.5820,
    # other fields like service, reference_weather_station are optional
}

resp = requests.post(url, json=payload, headers=headers)
print(resp.status_code, resp.json())
```

#### Expected response:

```json
{
  "location_id": "FAC-A",
  "site_name": "Facility A"
}
```

This confirms your load location is set up and mapped to your identifier.

---

### Using the alitiq SDK (Python)

If you're using the SDK, here's how to do it:

```python
from alitiq import alitiqLoadAPI
from alitiq.models.load_forecast import LoadLocationForm

# Initialize client
load_api = alitiqLoadAPI(api_key="your-api-key")

# Define location using Pydantic model
location = LoadLocationForm(
    site_name="Facility A",
    location_id="FAC-A",
    latitude=48.1351,
    longitude=11.5820,
    service="electricity-load"  # Optional; defaults to "electricity-load"
)

# Create the location
response = load_api.create_location(location)
print("Created load location:", response)
```

The SDK ensures your data is validated before sending—latitude/longitude ranges, empty names, and incorrect enums will be caught early.

---

### Inspect your portfolio

List all defined load locations via API:

```python
resp = requests.get(
    "https://api.alitiq.com/load/location/list/",
    headers={"x-api-key": "your-api-key"},
    params={"response_format": "json"}
)
print(resp.json())
```

Or, using the SDK:

```python
df = load_api.list_locations()
print(df)
```

You'll get a structured table of all your locations, complete with `site_name`, `location_id`, coordinates, and timestamps.

---

### Takeaways

| Action                                       | Benefit                                        |
| -------------------------------------------- | ---------------------------------------------- |
| Define **site\_name** and **coordinates**    | Precisely geolocate your forecast target       |
| Use **optional external ID** (`location_id`) | Maintain consistent references in your records |
| Use SDK's `LoadLocationForm`                 | Leverage built-in validation and cleaner code  |
| List locations                               | Quickly audit and manage your portfolio        |

Defining load locations correctly ensures reliable integrations with measurements and forecasts—and sets the stage for smarter energy management.

---

**Need help or feedback?** Reach out to [support@alitiq.com](mailto:support@alitiq.com)

---

Let me know if you'd like tweaks to tone, length, or code examples!
