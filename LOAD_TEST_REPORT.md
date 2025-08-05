# 📊 Load Test Report – Penguin Species Prediction API

## ✅ Overview

This report summarizes the load testing results of our FastAPI-based Penguin Prediction API deployed to **Cloud Run**. Tests were performed using **Locust**.

---

## ⚙️ Test Configuration

- **Tool:** Locust
- **Endpoint Tested:** `/predict`
- **Cloud Run URL:** `https://penguin-apii-941721411939.us-central1.run.app`
- **Payload Example:**
  ```json
  {
    "bill_length_mm": 39.5,
    "bill_depth_mm": 17.4,
    "flipper_length_mm": 186.0,
    "body_mass_g": 3800.0
  }
Load Test Summary
Test Type	Avg Response Time (ms)	Failure Rate	Requests per Second
Baseline	52.53	0%	32
Normal Load	50.74	0%	1404
Stress Test	48.87	0%	2999
Spike Test	54.02–61	0%	975–15

Response times remained consistent and low, even under stress and spike tests.
Failure rate was 0% in all scenarios — your Cloud Run service handled traffic very reliably.
Spike Test Insight: Even with sudden user surges (1 to 100 users), the system did not crash or time out.

Recommendations
✅ No changes required for current load.
🔭 For real-world traffic, consider auto-scaling settings on Cloud Run.
📈 Monitor longer-term performance using GCP metrics (CPU/memory).