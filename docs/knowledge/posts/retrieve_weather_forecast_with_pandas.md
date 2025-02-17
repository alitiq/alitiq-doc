---
date: 2025-02-17
authors: [alitiq]
categories:
  - IO
---

# Retrieve Weather Forecasts from alitiq-API with python and pandas 🌤️

Parsing weather forecasts from our Weather API is easy and just needs some lines of code. You need to know which weather forecasting model and the location you want to get forecasts for. 


<!-- more -->


```python
import pandas as pd
import requests
from io import StringIO

#  configure the request # 
weather_model= 'icon_eu'  # without weather_model you will receive mos_mix forecast for the closest location
response_format= 'json'  # alternative: csv or html
api_token= '' # add your token here 
latitude, longitude = 49.23247790, 6.98900836
# zip_code = 86424
# city_name = 'Munich'

# query api # 
response = requests.get(
    f"https://api.alitiq.com/weather_forecast/?"
    f"latitude={latitude}&"
    f"longitude={longitude}&"
    f"weather_model={weather_model}&"  # comment this line to retrieve mos_mix forecast as default 
    f"response_format={response_format}",
    headers={'x-api-key': api_token},
    verify=True
)
data = pd.read_json(StringIO(response.text), orient='split')

```

Further information can be found [here](https://docs.alitiq.com): 