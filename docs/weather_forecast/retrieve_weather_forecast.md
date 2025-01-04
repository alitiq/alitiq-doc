# Retrieving Weather Forecasts 🌤️

The endpoint for retrieving weather forecasts is:

```
https://api.alitiq.com/weather_forecast/
```

This endpoint requires the following parameters:

| Parameter         | Description                                                                                              | Type   |
|-------------------|----------------------------------------------------------------------------------------------------------|--------|
| **latitude**      | *Optional.* WGS84 coordinates in the north-south direction (e.g., Google Maps coordinates).              | float  |
| **longitude**     | *Optional.* WGS84 coordinates in the east-west direction (e.g., Google Maps coordinates).                | float  |
| **zip_code**      | *Optional.* Postal code within Germany. The geographic center of the respective postal code area will be used as the reference point for data retrieval. Example: `86153` | string |
| **city_name**     | *Optional.* City or location names in English. Ensure correct spelling for successful geolocation. Examples: `Munich`, `Augsburg`, `Berlin`, `London`, `Paris`. | string |
| **response_format** | The output format. Options are `html`, `csv`, `json`. CSV and JSON follow standard pandas DataFrame formats. | string |

---

### Optional: Selecting the Weather Forecast Model

| Parameter        | Description                                                                                                                                                                            | Type   |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| **weather_model** | Specifies which weather forecast model to use. Options are: `icon_d2`, `icon_eu`, `icon`, `icon_global`, `harmonie_knmi`, `mos_mix`. Default value: `mos_mix`.                          | string |

**Note:**  
The `icon` model is a combination of the high-resolution forecast model `icon_d2` (forecast horizon: 48 hours) and the broader `icon_eu` model (forecast horizon: 120 hours).

- The first 48 hours are provided by `icon_d2`.  
- For the remaining 72 hours, the `icon_eu` model is used, ensuring a seamless forecast period of up to 120 hours.

---

## Time Aggregated Forecasts

For presenting forecasts on a daily basis or at other intervals, another endpoint is available:

```
https://api.alitiq.com/weather_forecast/aggregation/
```

This endpoint requires an additional parameter:

| Parameter | Description                                                                                                 | Type   |
|-----------|-------------------------------------------------------------------------------------------------------------|--------|
| **freq**  | Specifies the frequency (interval) of the forecast.                                                         | string |
|           | **Examples:**                                                                                               |        |
|           | - For daily forecasts: `1D`                                                                                |        |
|           | - For 3-hour forecasts: `3H`                                                                               |        |

---

### Example Request:
```bash
https://api.alitiq.com/weather_forecast/aggregation/?latitude=51.2288286&longitude=6.7734849&freq=1D
```

---

### Explanation of `weather_synop_code`

We have translated the synoptic coding `weather_synop_code`, which represents the current weather condition, into more comprehensible terms. The return value of `weather_synop_code_icons` corresponds to weather icons, which you can find [here](#).  

These are based on the `weather_synop_code` from the **WMO (World Meteorological Organization)**. You can find a detailed mapping of the significant weather codes [here](#).


### Behavior of the API according to your location specification

For requests, the API determines the nearest location (`mos_mix`) or the closest grid point (for other models) based on the provided coordinates. All available data for the selected model is always returned.

#### Example Request:
```bash
https://api.alitiq.com/weather_forecast/?latitude=48.356&longitude=10.904&response_format=json&weather_model=mos_mix
```

### Example html response Plot

![Weather Forecast](/assets/example_html_plot_weather_forecast.png)