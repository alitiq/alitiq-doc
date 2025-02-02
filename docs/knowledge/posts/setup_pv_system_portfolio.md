---
date: 2025-02-02
authors: [alitiq]
categories:
  - Solar-APP
---

# ⚡ Setup your PV-System for Solar Power Forecast @ alitiq

In our general Documentation about the API [here](https://docs.alitiq.com/solar_power_forecast/setup_pv_portfolio_forecast), we described the way to setup / configure your PV-System in a high-level way. To give you a more detailed view into the way we think about PV-Systems and how you can boost the performance by just following this guide, keep reading. 

## Locations and Subsystems

Each PV-System is defined by it `location` and 1 or more `subsystems`. A PV-System is divided into subsystems by unique combinations of the **azimuth** (or module orientation) and **tilt** (or slope) of the modules. Maybe, this will differ from the inverter and string setup. 

![alitiq PV-System azimuth and tilt](/docs/assets/azimuth_tilt.png)


> Please note, that we ask for measurements for a System and not for a Subsystem, which means we only interest in the outcome of the whole PV-System in case you are interested in receiving optimized forecast. 

So just find out your different **azimuth** and **tilt** combinations and split up the inverter and module power according to the share of the installed power of the whole system. 

The `location` has to defined once for each subsystem in the upper section of the configuration panel. 

![alitiq Location definition](/docs/assets/location.png)


## Azimuth 

We have defined that a southern azimuth equals 180 °. A northern azimuth equals 0 °or 360 °. An azimuth to the west is 270 ° and to the east 90 °. There is noe difference between Northern or Southern hemisphere. So PV-Systems in Australia facing to the north have the azimuth 0 °. 

![Image](/docs/assets/compass_above_system.png)



## Example 
![Image](/docs/assets/roof_top_example.png)


We assume the system, you can see in the image above, has an installed module capacity of 100 kWp and an installed inverter capacity of 80 kWp. 70 % belongs to the left roof and 30 % to the right roof. From the specifications we know the tilt of the pv modules is 10 °. This means that this PV-System splits up into 4 Subsystems and here is how:


1. Left-Roof: Module azimuth of 93 ° and tilt 10 ° , with 35 % of 100 kWp installed capacity is 35 kWP and 28 kWp inverter capacity 
2. Left-Roof: Module azimuth of 273 ° and tilt 10 ° , with 35 % of 100 kWp installed capacity is 35 kWP and 28 kWp inverter capacity 
3. Right-Roof: Module azimuth of 96 ° and tilt 10 ° , with 15 % of 100 kWp installed capacity is 15 kWP and 12 kWp inverter capacity
4. Right-Roof: Module azimuth of 276 ° and tilt 10 ° , with 15 % of 100 kWp installed capacity is 15 kWP and 12 kWp inverter capacity


## Tracking

 ![Image](/docs/assets/tracking_config.png)
Setting up a system with a tracking is a bit more complex compared to the other. First of all you have to know the type of the tracking. We differ between:

1. No Tracking
2. Vertical Axis Tracking
3. Horizontal Axis Tracking
4. Dual Axis Tracking

In case your system runs with a backtracking algorithm to reduce shading in the morning and evening hours, turn on the radio button. 
The other parameters (table length, height and row distance are important for the backtracking algorithm). 

## Boosting your PV forecast performance?

In case you are unable to share near realtime data from your pv system with us, your forecast will derived by default according to the configuration you have made in our portal. As much more accurate the setup is, the more accurate the forecast will be. And even when you provide measurements from your pv systems, the initial guess or baseline forecast will help our machine learning and artifical intelligence algorithms to derive more accurate forecasts for your. 


