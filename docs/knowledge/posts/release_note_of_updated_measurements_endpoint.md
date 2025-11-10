---
date: 2025-11-10
authors: [alitiq]
categories:
  - IO
---

# Release Note — Measurements & Curtailments Endpoints

**Affected Routes:**  

- `POST /solar/measurement/add/`
- `POST /wind/measurement/add/`
- `POST /load/measurement/add/`
- `POST /solar/curtailments/add/`
- `POST /wind/curtailments/add/`


<!-- more -->

---

## ✨ Summary
The **measurements and curtailments endpoints** for solar, wind, and load have been updated to support **timezone-aware timestamps**.  

Previously, timestamps were required to be **naive (UTC-based)**, and a separate optional `timezone` parameter defined the timezone context — defaulting to UTC. This behavior has been **changed**.

---

## 🔄 What’s New

- **Timezone-aware timestamps are now accepted** directly in the request payload.  
- The `timezone` parameter **remains available but is no longer optional** — a missing or invalid timezone may now cause an error.  
- The **default UTC fallback has been removed.**  
  - If no timezone is provided (and timestamps are not timezone-aware), the request may be rejected.  
- Improved validation for timestamp handling via the `handle_timezone_awareness()` utility.  
- Consistent timezone handling across **solar**, **wind**, and **load** endpoints.

---

## ⚠️ Potential Breaking Change
Requests that previously relied on **implicit UTC handling** (i.e., without a timezone) may now fail unless:
- timestamps are explicitly **timezone-aware**, or  
- a valid `timezone` parameter is provided in the payload.

---

## ✅ Recommended Action
Review all integrations and ensure:
- All submitted timestamps include timezone information (e.g., `2025-11-10T12:00:00+01:00`), **or**
- The `timezone` field is explicitly set in the request.

---

