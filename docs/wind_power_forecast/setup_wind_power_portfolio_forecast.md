# Solar-PV power forecasting locations

Welcome to the **alitiq Wind Power Forecasting API**! This guide explains how to create a location for a WindPark including an individual amount of turbines for your WindPark location.  

---

## Key Concepts 📚  

Here’s your optimized and completed markdown:  

---

In the **alitiq Wind API**, a **WindPark** is represented as a location with one or more **wind turbines**. Forecasts are generated for an entire **WindPark**, not for individual turbines.  

A list of available wind turbines can be found **[here](https://docs.alitiq.com/wind_power_forecast/available_turbines_types)**.  

---

### **WindTurbineSchema**  
A **WindTurbine** is defined by the following parameters:  

- **Hub Height**: The height from the ground to the center of the turbine’s rotor (in meters).  
- **Rotor Diameter**: The total diameter of the turbine’s rotor blades (in meters) [Optional].  
- **Turbine Type**: The specific model or manufacturer identifier for the wind turbine.  
- **Installed Power**: The maximum rated power output of the turbine (in kilowatts)Required in case you decided to use "DEFAULT" turbine type.  

---

## Add a new WindPark to your portfolio 🚀  

To add a new location to your portfolio, you have to use the `wind_parks/add/` endpoint.

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/wind/wind_parks/add/"
    payload = {
      "location_id": "WP123",
      "latitude": 51.52079,
      "longitude": 7.75955194036,
      "site_name": "Test-site",
      #"zip_code": "59423",
      #"country": "DE",
      #"tso_area": "Tennet",
      #"nighttime_curtailment": True,
      #"start_nighttime_curtailment": "22:00:00",
      #"end_nighttime_curtailment": "06:00:00",
      #"curtailment_level": 0.3,
      #"time_zone_curtailment": "CET",
      "wind_turbines": [
          {
              "hub_height": 110.0,
              "rotor_diameter": 136.0,
              "turbine_type": "VS136/3500",
              "installed_power": 3500.0
          },
          {
              "hub_height": 110.0,
              "rotor_diameter": 136.0,
              "turbine_type": "VS136/3500",
              "installed_power": 3500.0
          }
      ]
    }
    headers = {"Content-Type": "application/json", "x-api-key": {api-key}}
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqWindAPI, WindParkModel
    
    # Initialize the API client
    wind_api = alitiqWindAPI(api_key="your-api-key")
    
    # Define the WindPark
    wind_park_data = {
      "location_id": "WP123",
      "latitude": 51.52079,
      "longitude": 7.75955194036,
      "site_name": "Test-site",
      #"zip_code": "59423",
      #"country": "DE",
      #"tso_area": "Tennet",
      #"nighttime_curtailment": True,
      #"start_nighttime_curtailment": "22:00:00",
      #"end_nighttime_curtailment": "06:00:00",
      #"curtailment_level": 0.3,
      #"time_zone_curtailment": "CET",
      "wind_turbines": [
          {
              "hub_height": 110.0,
              "rotor_diameter": 136.0,
              "turbine_type": "VS136/3500",
              "installed_power": 3500.0
          },
          {
              "hub_height": 110.0,
              "rotor_diameter": 136.0,
              "turbine_type": "VS136/3500",
              "installed_power": 3500.0
          }
      ]
    }
    
    # Create the location
    response = wind_api.create_location(WindParkModel(**wind_park_data))
    print("Location created:", response)
    ```

=== "cURL"

    ``` bash
    curl --request POST \
      --url https://api.alitiq.com/wind/wind_parks/add/ \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: {api-key}' \
      --data '{
        "location_id": "WP123",
        "latitude": 51.52079,
        "longitude": 7.75955194036,
        "site_name": "Test-site",
        "wind_turbines": [
            {
                "hub_height": 110.0,
                "rotor_diameter": 136.0,
                "turbine_type": "VS136/3500",
                "installed_power": 3500.0
            },
            {
                "hub_height": 110.0,
                "rotor_diameter": 136.0,
                "turbine_type": "VS136/3500",
                "installed_power": 3500.0
            }
        ]
      }'
    ``` 


---


## Inspect your portfolio 

After setting up your portfolio or to check out existing locations, you can use the `wind_parks/list/` endpoint.

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/wind/wind_parks/list/"
    
    querystring = {"response_format":"html"}
    
    payload = ""
    headers = {"x-api-key": {api-key}}
    response = requests.request("GET", url, data=payload, params=querystring, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqWindAPI
    
    # Initialize the API client
    wind_api = alitiqWindAPI(api_key="your-api-key")
    
    # return the location as a pd.DataFrame
    response = wind_api.list_locations()
    print("Locations:", response)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/wind/wind_parks/list/?response_format=json' \
      --header 'x-api-key: api-key'
    ``` 


Example response json: 
```json
{
  "columns":
  [
    "location_id",
    "altitude",
    "latitude",
    "longitude",
    "site_name",
    "zip_code",
    "country",
    "tso_area",
    "nighttime_curtailment",
    "start_nighttime_curtailment",
    "end_nighttime_curtailment",
    "curtailment_level",
    "time_zone_curtailment",
    "mrl_power",
    "eeg_key",
    "turbine_id",
    "hub_height",
    "rotor_diameter",
    "turbine_type",
    "installed_power"
  ],"index":[0,1],
  "data":[
    ["WP123",176.6,51.52,7.76,"Test-site",null,null,null,null,null,null,null,null,null,null,658,110.0,136.0,"VS136/3500",3500.0],
    ["WP123",176.6,51.52,7.76,"Test-site",null,null,null,null,null,null,null,null,null,null,659,110.0,136.0,"VS136/3500",3500.0]]
}
```

In the response of your portfolio you might find additional information that you have not defined e.g. the TSO-Area or a ZIP Code. These information are defined by alitiq.

In case you use the html- Response of the API the systems will be shown in a table like this: 

![html-overview API](https://docs.alitiq.com/assets/html_overview_api.png)

---

## Delete system from your portfolio

In case you want to delete a pv-system from your portfolio, you can simply use a POST request to the endpoint `wind_parks/delete/` it. Please use your individually defined location_id to delete the system: 

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/wind/wind_parks/delete/"
    
    querystring = {"location_id": "your-location-id-to-delete"}
    
    payload = ""
    headers = {"x-api-key": {api-key}}
    response = requests.request("POST", url, data=payload, params=querystring, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqWindAPI
    
    # Initialize the API client
    wind_api = alitiqWindAPI(api_key="your-api-key")
    
    # delete location 
    response = wind_api.delete_location("your-location-id-to_delete")
    print(response.text)
    ```

=== "cURL"

    ``` bash
    curl --request POST \
      --url 'https://api.alitiq.com/solar/pv_systems/delete/?location_id=your-location-id-to_delete' \
      --header 'x-api-key: api-key'
    ``` 

---


## FAQs ❓ 

### My turbine is not listed?

Feel free to contact us as [support@alitiq.com](mailto:support@alitiq.com)  . In the meantime, you can choose `DEFAULT` as turbine type, and submit an installed power. 

### Can I update the location later?  

Currently not, this feature is under development. Please `delete` the WindPark and re-configure it.

---

## Support & Feedback 💬  
- **Contact Support**: [support@alitiq.com](mailto:support@alitiq.com)  

🌟 **Start forecasting smarter with alitiq today!** 🌟  