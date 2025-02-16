# How to Inspect Measurement Data with the alitiq Load API 🔍  

The load forecasting API provides powerful tools to inspect and analyze the historical measurement data for your assets/portfolios. This feature allows you to validate submitted data, track system performance, and gain insights into your load characteristics.  

---

## Overview  

Inspecting data involves retrieving historical measurement records stored in the alitiq system for a specific load timeseries. You can define a time range, customize the output format, and perform detailed analysis on the retrieved data.

---

## Key Features ✨  

- **Flexible Time Ranges**: Retrieve data for any specified date range.  
- **Detailed Records**: Includes power output, timestamps, and optional irradiance values.  
- **Analysis Ready**: Data is returned in a format suitable for direct analysis using tools like pandas.  

---

## Required Parameters  

To inspect data, provide the following information:  

| **Parameter**   | **Type**          | **Description**                                                   | **Default**              |  
|------------------|-------------------|-------------------------------------------------------------------|--------------------------|  
| `location_id`    | `str`            | Unique identifier of the location whose data you want to inspect. | None                     |  
| `start_date`     | `datetime` (Optional) | Start date for the inspection range.                              | 2 days before today      |  
| `end_date`       | `datetime` (Optional) | End date for the inspection range.                                | Today                    |  

---

## Example: Inspect Data  

Below is an example of how to use the `measurement/inspect/` endpoint to inspect data and the method `get_measurements`:  


=== "python requests"

    ``` python
    import requests
    
    url = "https://api.alitiq.com/load/forecast/single/"
    
    querystring = {"location_id":"123","response_format":"json"}
    
    payload = ""
    headers = {"x-api-key": "api-key"}
    
    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)
    
    print(response.text)
    ```

=== "alitiq-py"

    ``` python
    from datetime import datetime, timedelta
    from alitiq import alitiqLoadAPI
    
    # Initialize the API client
    load_api = alitiqLoadAPI(api_key="your-api-key")
    
    # Define the location and date range
    location_id = "99"  # defined by alitiq
    start_date = datetime.now() - timedelta(days=7)  # 7 days ago
    end_date = datetime.now()  # Today
    
    # Inspect measurement data
    data = load_api.get_measurements(
        location_id=location_id, 
        start_date=start_date, 
        end_date=end_date
    )
    
    # Print the retrieved data
    print(data)
    ```

=== "cURL"

    ``` bash
    curl --request GET \
      --url 'https://api.alitiq.com/load/measurement/inspect/?location_id=123&response_format=json' \
      --header 'x-api-key: api-key'
    ``` 


---

## API Response  

The API returns the measurement data in a pandas-compatible format (e.g., JSON), which can be directly loaded into a DataFrame for further analysis:  

```plaintext
|       dt        |   power   |  timezone | interval_in_minutes | window_boundary |  
|-----------------|-----------|-----------|---------------------|------------------|  
| 2024-06-10 10:00|  120.5    |   UTC     | 15                  | end              |  
| 2024-06-10 10:15|  90.8     |   UTC     | 15                  | end              |  
| 2024-06-10 10:30|  150.0    |   UTC     | 15                  | end              |  
```  

---

## Best Practices  

- **Validate Data**: Regularly inspect your measurement data to ensure it is accurate and complete.  
- **Batch Analysis**: Retrieve data in chunks for longer periods to avoid API response size limitations.  
- **Timezone Awareness**: Ensure the `timezone` is consistent across measurements for accurate analysis.  

---

## Advanced Use Case: Data Visualization  

You can use tools like `matplotlib` or `seaborn` to visualize the data for insights:  

```python
import matplotlib.pyplot as plt

# Visualize power output over time
data.plot(x='dt', y='power', title="Power Output Over Time", figsize=(10, 6))
plt.show()
```  

---

## Notes  

- **Performance**: For large datasets, limit the date range to improve response time.  
- **Missing Data**: If any data points are missing, double-check your measurement submissions.  
- **Data Validation**: The SDK validates data upon submission to minimize errors during inspection.  

---

For further questions or issues, contact [support@alitiq.com](mailto:support@alitiq.com). 🌟  