# 🔆 **PV Simulation from Irradiance Observations**

This endpoint simulates the **power output of a PV system** for a past period, based on **satellite irradiance observations**. You send the configuration of a PV system and receive the simulated power time series right away.

The simulation runs on the fly. Nothing is stored, and the PV system doesn't need to be part of your portfolio. This makes it useful for:

* checking a PV system configuration before adding it to your portfolio
* estimating what a system should have produced, e.g. to detect underperformance or outages
* filling gaps in measured data with a physically based estimate

---

## ⚙️ **How it works**

1. **Irradiance**: global horizontal irradiance is taken from the same satellite data as the [Irradiance API](irradiance_data.md).
2. **Air temperature**: hourly observations of the closest weather station within 40 km, interpolated to the irradiance timestamps. If no station is available, a constant 15 °C is used.
3. **Simulation**: alitiq's PV model converts both into AC power, including module orientation, tracking, temperature losses and inverter clipping.

---

## 📥 **API Endpoint**

`POST https://api.alitiq.com/weather/irradiance/simulation/`

---

## 🔑 **Query Parameters**

| Parameter              | Type    | Description                                                                                                      |
| ---------------------- | ------- | ---------------------------------------------------------------------------------------------------------------- |
| `start_date`           | string  | Start datetime in UTC (ISO format, e.g., `2026-09-01T00:00:00`). Defaults to the last 24 hours if not provided.  |
| `end_date`             | string  | End datetime in UTC (ISO format, e.g., `2026-09-08T00:00:00`). Required if `start_date` is set.                  |
| `satellite`            | string  | `cm_saf_europe` (default, 10-minute values) or `cm_saf` (15-minute values). See the note below.                  |
| `interpolate_to_15min` | boolean | Interpolate the irradiance linearly to 15-minute values before the simulation (default: `false`).                |
| `response_format`      | string  | `json`, `csv`, or `html` (default: `json`). `html` returns a plot of the simulated power.                        |

---

## 📦 **Request Body**

The body takes the **same PV system configuration** as [adding a PV system to your portfolio](../solar_power_forecast/setup_pv_portfolio_forecast.md): a list with one entry per **subsystem** (unique combination of azimuth and tilt).

All subsystems must belong to **one site**, so they need the same `latitude` and `longitude`. The fields are validated in the same way as when adding a PV system, including the additional parameters for [tracking systems](../solar_power_forecast/setup_pv_portfolio_forecast.md#tracking-system).

| Field                      | Type   | Description                                                        |
| -------------------------- | ------ | ------------------------------------------------------------------ |
| `site_name`                | string | Name of the site                                                   |
| `latitude`                 | float  | Latitude of the site                                               |
| `longitude`                | float  | Longitude of the site                                              |
| `installed_power`          | float  | Installed module power of the subsystem (e.g. in kW)               |
| `installed_power_inverter` | float  | Installed inverter power of the subsystem, in the same unit        |
| `azimuth`                  | float  | Orientation of the modules (0–359°, South 180°)                    |
| `tilt`                     | float  | Tilt of the modules from the horizontal plane (in degrees)         |
| `temp_factor`              | float  | Optional temperature factor (default `0.03`)                       |
| `mover`                    | int    | Optional tracking type (default `1`, no tracking)                  |

---

## 📤 **Returned Data**

| Column                         | Unit                       | Description                                      |
| ------------------------------ | -------------------------- | ------------------------------------------------ |
| `power`                        | unit of `installed_power`  | Simulated AC power output of the whole site      |
| `global_horizontal_irradiance` | W/m²                       | Satellite irradiance used for the simulation     |
| `air_temperature_2m`           | °C                         | Air temperature used for the simulation          |

* **Interval**: the satellite's native interval (10 minutes for `cm_saf_europe`, 15 minutes for `cm_saf`), or 15 minutes with `interpolate_to_15min=true`
* **Timestamps**: UTC

---

## ⚠️ **Important Notes**

✅ The simulation reflects the satellite-derived irradiance, not on-site measurements. Local effects such as shading or soiling beyond the standard losses are not included.
✅ `cm_saf_europe` is available from **2026-07-10** onwards. For requests that start earlier, `cm_saf` is used automatically.
✅ Only available for locations within the satellite coverage (Europe, Africa).

---

## 🔧 **Example Request**

=== "python requests"

    ```python
    import requests
    import pandas as pd
    from io import BytesIO

    url = "https://api.alitiq.com/weather/irradiance/simulation/"

    querystring = {
        "start_date": "2026-09-01T00:00:00",
        "end_date": "2026-09-08T00:00:00",
        "interpolate_to_15min": True,
        "response_format": "json",
    }
    payload = [
        {
            "site_name": "My Solar Plant",
            "latitude": 48.16017,
            "longitude": 10.55907,
            "installed_power": 500,
            "installed_power_inverter": 480,
            "azimuth": 180,
            "tilt": 25,
        }
    ]
    headers = {"Content-Type": "application/json", "x-api-key": "your-api-key"}

    response = requests.request("POST", url, json=payload, headers=headers, params=querystring)
    data = pd.read_json(BytesIO(response.content), orient="split")
    ```

=== "alitiq-py"

    ```python
    from datetime import datetime
    from alitiq import alitiqSolarAPI, SolarPowerPlantModel

    solar_api = alitiqSolarAPI(api_key="your-api-key")

    plant = SolarPowerPlantModel(
        site_name="My Solar Plant",
        location_id="SP123",
        latitude=48.16017,
        longitude=10.55907,
        installed_power=500.0,
        installed_power_inverter=480.0,
        azimuth=180.0,
        tilt=25.0,
    )

    simulation = solar_api.simulate_pv_power(
        plant,
        start_date=datetime(2026, 9, 1),
        end_date=datetime(2026, 9, 8),
        interpolate_to_15min=True,
    )
    ```

=== "cURL"

    ```bash
    curl --request POST \
      --url 'https://api.alitiq.com/weather/irradiance/simulation/?start_date=2026-09-01T00:00:00&end_date=2026-09-08T00:00:00&interpolate_to_15min=true&response_format=json' \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: {api-key}' \
      --data '[
        {
            "site_name": "My Solar Plant",
            "latitude": 48.16017,
            "longitude": 10.55907,
            "installed_power": 500,
            "installed_power_inverter": 480,
            "azimuth": 180,
            "tilt": 25
        }
    ]'
    ```
