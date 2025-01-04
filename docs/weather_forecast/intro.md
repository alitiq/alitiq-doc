# 🌤️ alitiq Weather Forecast API 🌤️


The Alitiq Weather API provides access to current weather information and forecasts for any location worldwide. Weather data can be retrieved using geographic coordinates (WGS84) or a German postal code. Depending on the product, the data is interpolated to the nearest location or grid point of a forecasting product. Selected services also allow queries using a station ID. All API requests are secured via a **HEADER authentication method**.

Access restrictions are determined by the rules outlined in your contract. These restrictions may include limits on requests per second and per month. However, there are no limitations on the content retrieved.

alitiq reserves the right to make future changes to access permissions, including disabling specific API endpoints. This is especially relevant for API extensions.

---

## Registration 📃

To use the alitiq Weather API, you will receive credentials from alitiq, consisting of a secret key (`x-api-key`). This secret key must not be shared with third parties and must be included in the header of every request.

### Authentication

Authentication is performed using the `x-api-key` parameter in the request header. Below is an example of a request using the command-line tool **cURL**:

### Example Header:
```bash
curl -X GET 'https://api.alitiq.com/weather_forecast/?latitude=49.356&longitude=11.904&response_format=json&weather_model=icon_eu' \
-H 'x-api-key: <your-api-key>'
```

---

## Available API Endpoints

alitiq provides various API endpoints for accessing weather data:

- **Weather Forecasts:** `/weather_forecast/`
- **Weather Observations:** `/observation/` and `/observation_global/`
- **Solar Position:** `/solar/`
- **Nowcast (+2h Precipitation Forecast):** `/nowcast/precipitation/`
- **Nowcast (Current Precipitation):** `/nowcast/gridded_precipitation/`

### Time Format

All timestamps in the data index are provided in UTC and follow the ISO 8601 format, e.g., `2022-03-30T07:00:00.000Z`.

---