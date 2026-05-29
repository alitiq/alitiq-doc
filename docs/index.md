# Getting Started with alitiq APIs 🌟

Welcome to **alitiq’s Forecasting Services**, where innovation meets precision in solar PV and load forecasting (wind is coming soon ;). This guide provides an overview of alitiq’s APIs and a step-by-step approach to get started. Whether you're managing solar installations or planning for energy demand, alitiq offers robust solutions tailored to your needs.

---

## Overview of alitiq APIs 🛠️  

alitiq offers different services via `api.alitiq.com`:  

### 1. **Solar PV Forecasting API** 🌞 
Designed for managing and forecasting solar power plants, this API provides:  

- **Portfolio Management**: Add, update, or remove PV systems.  
- **Power Forecasting**: Retrieve accurate solar power forecasts for individual locations or entire portfolios.  
- **Measurement Management**: Push real-time or historical data for more precise forecasting.  

The endpoint for this service is `api.alitiq.com/solar`

### 2. **Load Forecasting API** 🔋
Optimized for heat, gas, and electricity forecasting, this API enables: 

- **Energy Load Predictions**: Obtain detailed forecasts for individual locations.  
- **Measurement Inspection**: Retrieve historical data for analysis.  
- **Custom Models**: Leverage alitiq’s optimized forecasting models for enhanced accuracy.  

The endpoint for this service is `api.alitiq.com/load`

### 3. **Weather Forecasting API** 🌤️
Weather is our profession but not our business. Eitherways weather data is a basis for our enhanced forecasts. So we make available any kind of weather information via out Weather API. 

- **Weather Forecast**: Obtain weather forecasts for individual locations from several leading national weather services.  
- **Weather Observations**: Access a global network of weather observations ranging from remote sesnsing (radar, satellite) to point observations 

The endpoint for this service is `api.alitiq.com/weather`

---

## How to Get Access 🔑  

The standalone solar portal has been discontinued. Portfolio management is now available directly in the API GUI at **[https://api.alitiq.com/gui](https://api.alitiq.com/gui)**.

### **Solar PV | Wind Forecasting API + GUI** 🌞
- **Step 1**: Contact **[sales@alitiq.com](mailto:sales@alitiq.com)** for API access and pricing information.  
- **Step 2**: Once approved, you’ll receive your `x-api-key` and relevant details.  
- **Step 3**: Open **[https://api.alitiq.com/gui](https://api.alitiq.com/gui)** and authenticate with your API key.  
- **Step 4**: Manage both your PV and wind portfolios directly in the GUI or use the endpoints via SDK/API.  


### **Load | Weather Forecasting API** 🔋
- **Step 1**: Contact **[sales@alitiq.com](mailto:sales@alitiq.com)** for API access and pricing information.  
- **Step 2**: Once approved, you’ll receive your API key and documentation tailored to your energy needs.  
- **Step 3**: Use the SDK or API to push measurements, retrieve forecasts, and manage demand analytics.  

---

## Security with `x-api-key` 🔒  

The alitiq Solar API uses the `x-api-key` for authentication and portfolio mapping. This key is unique to each user and is required to access the API. It ensures that:  

1. **Portfolio Mapping**: The `x-api-key` links your requests to the correct portfolio, ensuring you access only your Solar PV systems and associated data.  
2. **Restricted Access**: Only users with the correct `x-api-key` can access your portfolio.  

### Keep Your `x-api-key` Safe  
To maintain the security and confidentiality of your portfolio:  
- **Do not share your API key** with unauthorized individuals.  
- **Store it securely**, such as in environment variables or a secure credentials manager.  
- **Regenerate your API key** immediately if you suspect it has been compromised.  

Your `x-api-key` is the gateway to your portfolio—keep it protected to ensure your data stays safe.  

---


## What’s Next? 🚀  

Once you have your API key:  
1. Install the `alitiq-py` SDK:  
   ```bash
   pip install alitiq
   ```  
2. Follow the [Quickstart Guide](#quickstart) to set up your first integration.  
3. Explore the [API Documentation](https://alitiq.com/api-docs) (coming soon) for advanced use cases.  

---

## Need Help? 🤔  

For further assistance:  
- Contact us at **[support@alitiq.com](mailto:support@alitiq.com)** for technical queries.  
- Reach out to **[sales@alitiq.com](mailto:sales@alitiq.com)** for load forecast-related inquiries.  

🌟 **Start forecasting smarter with alitiq today!** 🌟