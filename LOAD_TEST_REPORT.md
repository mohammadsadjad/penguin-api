# 📊 Load Test Report – Penguin Species Prediction API

##  Overview

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
##Test Results Summary

Scenario	Avg Response Time (ms)	Failure Rate (%)	Requests/sec
Baseline	52.53	0	32
Normal Load	50.74	0	1404
Stress Test	48.87	0	2999
Spike Test	54.02 – 61	0	15 – 975
## Analysis

Consistency: The API demonstrated stable performance across all scenarios, with response times remaining under 61 ms.
Scalability: The service handled over 2,900 RPS during the stress test without any failure, showcasing strong scalability on Cloud Run.
Spike Handling: During the spike test, response times slightly increased (~61 ms max) but still within acceptable limits.
Failure Rate: 0% failure rate in all test cases — excellent reliability.
💡 Bottlenecks & Observations
No bottlenecks observed during testing.
Minor latency increase in spike tests likely due to autoscaling warm-up time.
Cloud Run auto-scaling responded well even under high concurrency.


 ##Recommendations
Autoscaling: Cloud Run autoscaling appears effective — no action needed for this scale.
Monitoring: Set up real-time monitoring and alerts using Cloud Monitoring for production environments.
Caching: Consider caching responses for repeated inputs to reduce model inference time (if traffic increases further).
Advanced Tests: For future work, include chaos testing and latency injection to simulate real-world outages or slowness.
##Conclusion
The Penguin Predictor API on Cloud Run is production-ready for moderate to high loads. With 0% failure and low latency even under stress and spike conditions, the deployment meets performance and reliability expectations.
