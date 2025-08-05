# 🐧 Penguin Species Prediction API

This project is a machine learning application that predicts the species of penguins using a trained XGBoost model served via a FastAPI web service.

---

## 📦 Features

- ML model trained on the Palmer Penguins dataset
- XGBoost classifier saved as `model.json`
- REST API built with FastAPI
- Dockerized for portability
- Model loaded from Google Cloud Storage (GCS)
- Deployed to Google Cloud Run
- Load tested using Locust

---

## 🚀 Live Demo

API URL: [https://penguin-apii-941721411939.us-central1.run.app](https://penguin-apii-941721411939.us-central1.run.app)

Try the `/predict` endpoint using POST:

```json
{
  "bill_length_mm": 39.5,
  "bill_depth_mm": 17.4,
  "flipper_length_mm": 186.0,
  "body_mass_g": 3800.0
}

Example response:

{
  "prediction": "Adelie"
}
Installation & Running Locally
# Clone the repo
git clone https://github.com/mohammadsadjad/penguin-api.git
cd penguin-api

# Create virtual environment
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Run the API
uvicorn main:app --host 0.0.0.0 --port 8080
Running Tests
pytest --cov=.
All tests are located in the tests/ folder. Test coverage includes:
Valid predictions
Missing fields
Invalid data types
Edge cases
Docker Instructions:
# Build Docker image
docker build -t penguin-api .

# Run Docker container
docker run -p 8080:8080 penguin-api

Cloud Deployment
✅ Uploaded Model to GCS:
Bucket: penguin-models-2025
Blob: model.json
Built & Pushed Image:
gcloud builds submit --tag us-central1-docker.pkg.dev/penguin-api-project/penguin-repo/penguin-api:latest
gcloud builds submit --tag us-central1-docker.pkg.dev/penguin-api-project/penguin-repo/penguin-api:latest
gcloud run deploy penguin-apii \
  --image=us-central1-docker.pkg.dev/penguin-api-project/penguin-repo/penguin-api:latest \
  --platform=managed \
  --region=us-central1 \
  --allow-unauthenticated \
  --set-env-vars=GCS_BUCKET_NAME=penguin-models-2025,GCS_BLOB_NAME=model.json

Load Testing
Load testing done with Locust:
Baseline: 1 user, 60 sec — 32 RPS
Normal Load: 10 users, 5 min — 1404 RPS
Stress Test: 50 users, 2 min — 2999 RPS
Spike Test: 1 → 100 users — 15–975 RPS
See full details in LOAD_TEST_REPORT.md.
🛡️ Security
API is deployed with unauthenticated access (for testing).
Service account key stored securely and excluded from version control via .gitignore.
📈 Monitoring
Used GCP Logs Explorer for error/debug monitoring
Verified successful startup and requests via logs
❓ Questions Answered
❓ What edge cases might break your model in production?
→ Extremely small/large or negative values can cause invalid predictions.
❓ What happens if your model file becomes corrupted?
→ The app raises a 500 error — handled in main.py.
❓ What's a realistic load for a penguin classification service?
→ 1000+ requests per second — confirmed with Locust.
❓ How would you optimize if response times are too slow?
→ Cache model in memory, use GPU-enabled backend, auto-scale Cloud Run.
❓ What metrics matter most for ML inference APIs?
→ Response time, success rate, resource usage, memory load.
❓ Why is Docker layer caching important?
→ It speeds up builds by reusing unchanged layers — yes, we leveraged it.
❓ What security risks exist with containers?
→ Containers running as root, exposed secrets — we mitigated these via read-only mount and .gitignore.
❓ How does cloud auto-scaling affect load test results?
→ Spike tests showed system adapting to traffic — Cloud Run handles scale well.
❓ What happens with 10x more traffic?
→ Auto-scaling will keep up, but latency might increase slightly.
❓ How would you monitor performance in production?
→ Stackdriver logs, custom metrics, alerting via GCP Monitoring.
❓ What is a blue-green deployment?
→ A release strategy to reduce downtime and rollback risk by having two environments (blue = live, green = staging).
❓ What if deployment fails?
→ Use logs to debug, roll back to last working revision.
❓ What happens if container uses too much memory?
→ Cloud Run will restart the container or throttle — should increase memory allocation.
