---
date: 2025-07-23
authors: [alitiq]
categories:
  - IO
---

# Why Understanding Curtailments and Unavailabilities Matters for Power Forecasting ⚡🌬️

In the quest for accurate wind power forecasting, there's one reality that often gets in the way: **real-world power output does not always reflect the full capacity of your wind turbines** or **pv systems**. This discrepancy is frequently caused by *curtailments* and *unavailabilities*.

<!-- more -->

At **alitiq**, we prioritize forecasting based on **true system potential**, not reduced or distorted generation. Here's why it matters — and what we do to ensure our forecasts are always a true representation of full operational availability.

---

## What Are Curtailments and Unavailabilities?  

### Curtailments  
Curtailments refer to **intentional reductions** in wind power output. This can be due to:
- Grid constraints  
- Market signals  
- Maintenance needs  
- Safety or compliance regulations

Even though the wind is blowing and the turbines could produce energy, they’re **instructed not to**.

### Unavailabilities  
Unavailabilities are **unplanned or planned outages** in renewable energy generation:
- Turbine failures
- Inverter failures
- Scheduled maintenance
- Communication breakdowns  
- Sensor issues or data gaps
- Damage due to severe weather

These events result in **zero or reduced output**, but not because of environmental or performance limitations.

---

## Why Forecasting Needs Clean Training Data  

If we trained our forecasting models on raw generation data that includes curtailments or unavailabilities, the results would be:
- **Underestimated forecasts**, because the model "learns" that the site often produces less than potential.
- **Erroneous correlations**, where the model mistakenly attributes reductions to weather or other valid features.
- **Poor generalization**, especially when turbines or pv system return to full service.

---

## alitiq’s Approach: Always Forecasting 100% Availability  

At alitiq, we **mask** curtailed or unavailable data in our training pipeline. This ensures that:
- Our models only learn from **valid, fully available** system behavior.  
- Forecasts reflect **what the system *could* produce**, not what it *did* produce under constraints.  
- You get a forecast for **ideal availability**, giving operators a baseline to measure performance, efficiency, or lost revenue.

This approach allows for:
- More **reliable capacity planning**  
- Better **grid interaction** and reserve allocation  
- Accurate **performance benchmarking**  

---

## How You Can Help Improve Forecast Accuracy  

To get the best from your forecasts, we recommend:
1. **Reporting curtailments**: Use our `/curtailments/add/` endpoint to provide structured curtailment data. It exists both for wind and solar.
2. **Marking unavailabilities**: Let us know when turbines or the pv system are out of service.
3. **Pushing complete measurement data**: Even historical values can improve learning.

By integrating curtailments and unavailabilities into your data pipeline, you're actively contributing to **cleaner, smarter forecasts**.

---

## Conclusion  

Forecasting isn’t just about knowing the solar irradiance or the wind — it’s about understanding when your system isn’t playing at full strength.

At alitiq, we’re committed to providing **100% availability forecasts** that you can rely on. Masking curtailments and unavailabilities is just one of the many ways we make our predictions smarter, fairer, and more actionable.

For any questions or integration support, reach out at [support@alitiq.com](mailto:support@alitiq.com) — we’re here to help! 💬

---

