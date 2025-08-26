# Solar-PV power forecasting locations

Welcome to the **alitiq Solar Power Forecasting API**! This guide explains how to create a location for a PV power plant, including subsystems for each unique combination of **azimuth** and **tilt**.  

---

## Key Concepts 📚  

In the alitiq Solar API, a **PV power plant** is represented as a location with one or more **subsystems**. Each subsystem corresponds to a unique configuration of azimuth and tilt of the PV modules. By defining these subsystems, the API ensures precise forecasting for the entire power plant.  


### Subsystems  
- A **subsystem** is defined by:  
  - **Azimuth**: Orientation of the module relative to true north (in degrees, South 180°).  
  - **Tilt**: Angle of the module from the horizontal plane (in degrees).  
  - **Power Capacity**: Installed capacity of the modules in the subsystem (in kW).  
  - **installed_power**: The capacity of all modules per subsystem in the power plant.  
  - **inverter_power**: The capacity of the inverters per subsystem in the power plant.  


- Each unique combination of azimuth and tilt requires a separate subsystem for accurate forecasting.  


---

## Add a new PV systems to your portfolio 🚀  

To add a new location to your portfolio, you have to use the `pv_systems/add/` endpoint.

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/solar/pv_systems/add/"
    
    payload = [
        {
            "location_id": "12",
            "site_name": "test_2",
            "latitude": 48.9,
            "longitude": 10.3,
            "installed_power": 320,
            "installed_power_inverter": 300,
            "azimuth": 180,
            "tilt": 13,
            "temp_factor": 0.033,
            "mover": 1
        },
        {
            "location_id": "12",
            "site_name": "test_2",
            "latitude": 48.9,
            "longitude": 10.3,
            "installed_power": 320,
            "installed_power_inverter": 300,
            "azimuth": 180,
            "tilt": 15,
            "temp_factor": 0.033,
            "mover": 1
        }
    ]
    headers = {"Content-Type": "application/json", "x-api-key": {api-key}}
    
    response = requests.request("POST", url, json=payload, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqSolarAPI, SolarPowerPlantModel
    
    # Initialize the API client
    solar_api = alitiqSolarAPI(api_key="your-api-key")
    
    # Define the PV power plant with subsystems
    plant = SolarPowerPlantModel(
        site_name="My Solar Plant",
        location_id="SP123",
        latitude=48.160170,
        longitude=10.55907,
        installed_power=1000.0,
        installed_power_inverter=950.0,
        azimuth=180.0,
        tilt=25.0,
    )
    
    # Create the location
    response = solar_api.create_location(plant)
    print("Location created:", response)
    ```

=== "cURL"

    ``` bash
    curl --request POST \
      --url https://api.alitiq.com/solar/pv_systems/add/ \
      --header 'Content-Type: application/json' \
      --header 'x-api-key: {api-key}' \
      --data '[
        {
            "location_id": "12",
            "site_name": "test_2",
            "latitude": 48.9,
            "longitude": 10.3,
            "installed_power": 320,
            "installed_power_inverter": 300,
            "azimuth": 180,
            "tilt": 13,
            "temp_factor": 0.033,
            "mover": 0
        },
        {
            "location_id": "12",
            "site_name": "test_2",
            "latitude": 48.9,
            "longitude": 10.3,
            "installed_power": 320,
            "installed_power_inverter": 300,
            "azimuth": 180,
            "tilt": 15,
            "temp_factor": 0.033,
            "mover": 0
        }
    ]'
    ``` 
!!! note

    After you have created your first or new pv system, it takes up to 6 hours to receive a first forecast under `optimized`. When you do not provide measurement data, the `optimized` is just a baseline forecast. No optimisation was done int htat case. Baseline forecast under `icon_eu` or `icon_global` is available with a delay of 5 minutes after creation.
    Optimized forecast are available the next day in case you have provided measurement data from the system.

---

#### Tracking system

Tracking systems are more advanced components in PV system modeling and require additional configuration details to accurately simulate system behavior.

The supported tracking types are:

* **No Tracking**: `0` or `1`
* **Single Axis Tracking (Vertical Axis)**: `2`
  *(Note: This is very rare and currently not supported.)*
* **Single Axis Tracking (Horizontal Axis)**: `3`
  *(This is the most common type.)*
* **Dual Axis Tracking**: `4`
  *(Rare, but supported.)*

##### Dual Axis Tracking

For dual-axis systems, no additional geometric parameters are needed. The modules follow the sun's position in both azimuth and zenith, offering optimal irradiance capture throughout the day.

##### Single Axis Tracking

For horizontal single-axis tracking systems (type `3`), the following parameters must be provided:

* **`table_length`**: Length of the PV table (in meters)

* **`height`**: Height of the rotation axis of the pv table (in metres)

* **`row_distance`**: Distance between adjacent tracker rows (in meters)
  These two parameters are used to calculate the *Ground Coverage Ratio (GCR)*.

* **`do_backtracking`**: Boolean flag indicating whether backtracking is enabled
  *(Backtracking reduces shading between rows during early morning and late afternoon.)*

* **`max_rotation_angle`**: The maximum rotation angle (in degrees) allowed for the tracker

##### System Alignment Notes

Adapt the following parameters based on your system configuration:

* If your tracker rows are aligned **north-south** (most common), set the **`azimuth` or `orientation`** to **180°**
* For systems installed on **flat ground**, set the **`tilt`** to **0°**


## Inspect your portfolio 

After setting up your portfolio or to check out existing locations, you can use the `pv_systems/list/` endpoint.

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/solar/pv_systems/list/"
    
    querystring = {"response_format":"html"}
    
    payload = ""
    headers = {"x-api-key": {api-key}}
    response = requests.request("GET", url, data=payload, params=querystring, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqSolarAPI
    
    # Initialize the API client
    solar_api = alitiqSolarAPI(api_key="your-api-key")
    
    # return the location as a pd.DataFrame
    response = solar_api.list_locations()
    print("Locations:", response)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/solar/pv_systems/list/?response_format=json' \
      --header 'x-api-key: api-key'
    ``` 


Example response json: 
```json
{
  "columns": [
    "location_id",
    "altitude",
    "latitude",
    "longitude",
    "site_name",
    "zip_code",
    "country",
    "do_backtracking",
    "row_distance",
    "tso_area",
    "subsystem_id",
    "installed_power",
    "installed_power_inverter",
    "temp_factor",
    "azimuth",
    "tilt",
    "mover",
    "height",
    "table_length",
    "max_rotation_angle"
  ],
  "index": [
    0,
    1,
    2,
    3
  ],
  "data": [
    [
      "1",
      126.95,
      50.06,
      8.83,
      "Obertshausen",
      "63179",
      "DE",
      false,
      null,
      "Amprion",
      5599,
      709.3,
      636.0,
      0.03,
      195.0,
      10.0,
      1,
      null,
      null,
      null
    ],
    [
      "1",
      126.95,
      50.06,
      8.83,
      "Obertshausen",
      "63179",
      "DE",
      false,
      null,
      "Amprion",
      5759,
      999.38,
      480.0,
      0.03,
      180.0,
      15.0,
      1,
      null,
      null,
      null
    ],
    [
      "4507",
      557.75,
      48.9,
      10.3,
      "test_2",
      null,
      null,
      null,
      null,
      null,
      5796,
      320.0,
      300.0,
      0.03,
      50.0,
      15.0,
      1,
      null,
      null,
      null
    ]
  ]
}
```

In the response of your portfolio you might find additional information that you have not defined e.g. the TSO-Area or a ZIP Code. These information are defined by alitiq.

In case you use the html- Response of the API the systems will be shown in a table like this: 

![html-overview API](https://docs.alitiq.com/assets/html_overview_api.png)

---

## Delete system from your portfolio

In case you want to delete a pv-system from your portfolio, you can simply use a POST request to the endpoint `pv_systems/delete/` it. Please use your individually defined location_id to delete the system: 

=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/solar/pv_systems/delete/"
    
    querystring = {"location_id": "your-location-id-to-delete"}
    
    payload = ""
    headers = {"x-api-key": {api-key}}
    response = requests.request("POST", url, data=payload, params=querystring, headers=headers)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from alitiq import alitiqSolarAPI
    
    # Initialize the API client
    solar_api = alitiqSolarAPI(api_key="your-api-key")
    
    # delete location 
    response = solar_api.delete_location("your-location-id-to_delete")
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

### Which temp_factor should I use? 

The **temperature factor** (temp_factor) accounts for the temperature-related efficiency loss of PV systems. Use the appropriate value based on the type of mounting for accurate forecasting.  

| **System Type**        | **Description**                        | **Temp Factor (temp_factor)** |
|-------------------------|----------------------------------------|-------------------------------|
| Free-Mounted Systems    | Modules mounted on open frames with good ventilation | `0.03`                      |
| Roof-Mounted Systems    | Modules mounted on roofs with moderate ventilation | `0.035`                       |
| Roof-Integrated Systems | Modules integrated into the roof with limited ventilation | `0.05`                       |  

---


### What if my power plant has only one subsystem?  
You can omit the `subsystems` field and define the **azimuth**, **tilt**, and **installed_power** at the plant level.  

### Can I update the location later?

Currently not, this feature is under development. Please `delete` the system and re-configure it.

---

## Support & Feedback 💬  
- **Contact Support**: [support@alitiq.com](mailto:support@alitiq.com)  

🌟 **Start forecasting smarter with alitiq today!** 🌟  